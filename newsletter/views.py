from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.conf import settings
from .models import NewsSubscriber
from .forms import EmailForm

@login_required
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if not NewsSubscriber.objects.filter(email=email).exists():
            NewsSubscriber.objects.create(user=request.user, email=email)
            messages.success(request, 'Newsletter subscription is now active')
        else:
            messages.info(request, 'You are already subscribed')

        # Оставляем пользователя на той же странице
        return redirect(request.META.get('HTTP_REFERER', 'default_view'))

    return render(request, 'newsletter/subscribe.html')


@login_required
def unsubscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            subscriber = NewsSubscriber.objects.get(email=email, user=request.user)
            subscriber.delete()
            messages.success(request, 'You have been unsubscribed from the newsletter.')
        except NewsSubscriber.DoesNotExist:
            messages.info(request, 'You were not subscribed to the newsletter.')
        return redirect(request.META.get('HTTP_REFERER', 'default_view'))

    return render(request, 'newsletter/unsubscribe.html')


@user_passes_test(lambda u: u.is_superuser)
def send_newsletter(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            subscribers = NewsSubscriber.objects.values_list('email', flat=True)
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                subscribers,
                fail_silently=False,
            )
            messages.success(request, 'Newsletter has been sent successfully!')
            return redirect('send_newsletter')
    else:
        form = EmailForm()

    return render(request, 'newsletter/create_letter.html', {'form': form})