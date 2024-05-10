from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib import messages
from django.conf import settings
from datetime import datetime, timedelta
from .models import UserSubscription, Subscription

import stripe


def check_subscription(request):

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
                # messages.error(request, "Your subscription is expired. Please get a new one")

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
            }
            return render(request, 'lessons/buy_subscription.html', context)
        # Free subscription handler
        else:
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
    try:
        current_user = UserSubscription.objects.get(user=request.user)
        if current_user.subscribed:
            return render(request, 'lessons/lessons.html')
        else:
            return redirect('check_subscription')
    except UserSubscription.DoesNotExist:
        messages.info(request, 'You should be subscribed to view lessons')
        return redirect('check_subscription')