from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from datetime import datetime, timedelta
from .models import UserSubscription, Subscription, Lesson, Playlist
from .utils import fetch_youtube_thumbnail
from .forms import LessonForm, PlaylistForm, ManageSubscriptionForm
import stripe


def check_subscription(request):
    """ Checks if the user has a subscription and based on result shows subscriptions or lessons """

    if request.user.is_authenticated:
        try:
            current_user = UserSubscription.objects.get(user=request.user)

            if current_user.expiry_date:
                if current_user.expiry_date < datetime.now().date():  # Checking if the subscription is expired
                    current_user.subscribed = False
                    current_user.save()
                    messages.error(request, "Your subscription is expired. Please get a new one")
            else:
                current_user.subscribed = False
                current_user.save()

            if current_user.subscribed:
                return redirect('lessons')
        except UserSubscription.DoesNotExist:
            pass
    if request.user.is_superuser:  # Show all subscriptions to the admin (including disabled)
        subscriptions = Subscription.objects.all().order_by('duration')
    else:
        subscriptions = Subscription.objects.filter(is_active=True).order_by('duration')
        if request.user.is_authenticated:
            had_subscription = UserSubscription.objects.filter(user=request.user).first()
            if had_subscription:
                subscriptions = Subscription.objects.filter(is_active=True).exclude(price=0).order_by('duration')
    context = {
        'subscriptions': subscriptions,
    }
    return render(request, 'lessons/subscriptions.html', context)


def buy_subscription(request, subscription_id):
    """ Subscription checkout """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    subscription = Subscription.objects.get(id=subscription_id)

    if request.method == 'GET':

        if not subscription.is_active:  # prevent user from choosing inactive subscription in URL
            messages.error(request, "Subscription doesn't exist ")
            return redirect('check_subscription')

        if subscription.price:
            if subscription.promotional_price:
                total = subscription.promotional_price
            else:
                total = subscription.price
            stripe_total = round(total * 100)
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )
            context = {
                'subscription': subscription,
                'total': total,
                'stripe_public_key': stripe_public_key,
                'client_secret': intent.client_secret,
                'simple_message': True,
            }
            return render(request, 'lessons/buy_subscription.html', context)
        # Free subscription handler
        else:
            if not request.user.is_authenticated:
                messages.info(request, 'Please login or signup to get your free subscription')
                return redirect(request.META.get('HTTP_REFERER', '/'))
            existing_subscription = UserSubscription.objects.filter(user=request.user).first()
            # If user has been subscribed already
            if existing_subscription:
                messages.error(request, 'Sorry, this subscription is no longer available')
                return redirect(request.META.get('HTTP_REFERER', '/'))
            else:
                # Activation of the free subscription (once for each user)
                UserSubscription.objects.create(
                    user=request.user,
                    subscribed=True,
                    subscription_name=subscription.name,
                    start_date=datetime.now().date(),
                    expiry_date=datetime.now().date() + timedelta(days=subscription.duration)
                )
                messages.success(request, 'Your free subscription is active now!')
                return redirect('lessons')

    else:
        if request.user.is_authenticated:
            existing_subscription = UserSubscription.objects.filter(user=request.user).first()

            if existing_subscription:
                existing_subscription.subscription_name = subscription.name
                existing_subscription.subscribed = True
                existing_subscription.start_date = datetime.now().date()
                existing_subscription.expiry_date = datetime.now().date() + timedelta(days=subscription.duration)
                existing_subscription.save()
            else:
                UserSubscription.objects.create(
                    user=request.user,
                    subscribed=True,
                    subscription_name=subscription.name,
                    start_date=datetime.now().date(),
                    expiry_date=datetime.now().date() + timedelta(days=subscription.duration)
                )
            messages.success(request, 'Subscription purchased!')
            return redirect('lessons')
        else:
            messages.info(request, 'Please login or create an account')
            return redirect(request.META.get('HTTP_REFERER', '/'))


def show_lessons(request):
    """ Show all lessons """
    try:
        current_user = UserSubscription.objects.get(user=request.user)
        subscriptions = Subscription.objects.all()
        if current_user.subscribed:
            lessons = Lesson.objects.all().order_by('number')
            playlists = Playlist.objects.filter(lesson__isnull=False).distinct()

            all_playlists = Playlist.objects.all()

            default_cover_path = 'static/img/default_cover.jpeg'

            for lesson in lessons:
                if not lesson.cover_image:
                    if lesson.video_url:
                        thumbnail = fetch_youtube_thumbnail(lesson.video_url)
                        if thumbnail:
                            lesson.cover_image = thumbnail
                        else:
                            lesson.cover_image = default_cover_path
                    else:
                        lesson.cover_image = default_cover_path

                    lesson.save()

            context = {
                'lessons': lessons,
                'playlists': playlists,
                'all_playlists': all_playlists,
                'subscriptions': subscriptions,
            }
            return render(request, 'lessons/lessons.html', context)
        else:
            return redirect('check_subscription')
    except UserSubscription.DoesNotExist:
        messages.info(request, 'You should be subscribed to view lessons')
        return redirect('check_subscription')


def lesson(request, lesson_id):
    """ Shows chosen lesson """
    current_lesson = Lesson.objects.get(pk=lesson_id)
    all_lessons = Lesson.objects.filter(playlist=current_lesson.playlist)
    all_lessons = all_lessons.order_by('number')

    all_lessons_list = list(all_lessons)
    current_index = all_lessons_list.index(current_lesson)
    previous_lesson = None
    next_lesson = None
    btn_previous = False
    btn_next = False

    if current_index > 0:
        previous_lesson = all_lessons_list[current_index - 1].id
        btn_previous = True
    if current_index < len(all_lessons_list) - 1:
        next_lesson = all_lessons_list[current_index + 1].id
        btn_next = True

    if current_lesson.video_url:
        video_id = str(current_lesson.video_url.split("/")[:-1])
        video_id = str(video_id.split("?")[0])
    else:
        video_id = None


    context = {
        'lesson': current_lesson,
        'video_id': video_id,
        'btn_next': btn_next,
        'btn_previous': btn_previous,
        'next_lesson': next_lesson,
        'previous_lesson': previous_lesson,
    }
    return render(request, 'lessons/lesson.html', context)

@login_required
def add_lesson(request):
    """ Add a lesson to the lessons section """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added lesson!')
            return redirect(reverse('add_lesson'))
        else:
            messages.error(request, 'Failed to add lesson. Please ensure the form is valid.')
    else:
        form = LessonForm()

    template = 'lessons/add_lesson.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_playlist(request):
    """ Add a lessons playlist to the lessons section """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PlaylistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added playlist!')
            return redirect(reverse('add_playlist'))
        else:
            messages.error(request, 'Failed to add playlist. Please ensure the form is valid.')
    else:
        form = PlaylistForm()

    template = 'lessons/add_playlist.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_lesson(request, lesson_id):
    """ Edit a lesson """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[lesson.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = LessonForm(instance=lesson)
        messages.info(request, f'You are editing {lesson.name}')

    template = 'lessons/edit_lesson.html'
    context = {
        'form': form,
        'lesson': lesson,
    }

    return render(request, template, context)


@login_required
def delete_lesson(request, lesson_id):
    """ Delete lesson from the playlist """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    current_lesson = get_object_or_404(Lesson, pk=lesson_id)
    current_lesson.delete()
    messages.success(request, 'Lesson deleted!')
    return redirect(reverse('lessons'))


@login_required
def delete_playlist(request, playlist_id):
    """ Delete playlist """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    chosen_playlist = get_object_or_404(Lesson, pk=playlist_id)
    chosen_playlist.delete()
    messages.success(request, 'Playlist deleted!')
    return redirect(reverse('lessons'))


@login_required
def add_subscription(request):
    """ Add a subscription for lessons """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ManageSubscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added subscription!')
            return redirect(reverse('add_subscription'))
        else:
            messages.error(request, 'Failed to add subscription. Please ensure the form is valid.')
    else:
        form = ManageSubscriptionForm()

    template = 'lessons/add_subscription.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_subscription(request, subscription_id):
    """ Edit a subscription """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    subscription = get_object_or_404(Subscription, pk=subscription_id)
    if request.method == 'POST':
        form = ManageSubscriptionForm(request.POST, request.FILES, instance=subscription)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated subscription!')
            return redirect(reverse('lessons'))
        else:
            messages.error(request, 'Failed to update subscription. Please ensure the form is valid.')
    else:
        form = ManageSubscriptionForm(instance=subscription)
        messages.info(request, f'You are editing {subscription.name}')

    template = 'lessons/edit_subscription.html'
    context = {
        'form': form,
        'subscription': subscription,
    }

    return render(request, template, context)


@login_required
def delete_subscription(request, subscription_id):
    """ Delete subscription """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    chosen_subscription = get_object_or_404(Subscription, pk=subscription_id)
    chosen_subscription.delete()
    messages.success(request, 'Subscription deleted!')
    return redirect('lessons')



