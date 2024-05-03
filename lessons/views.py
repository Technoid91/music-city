from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime, timedelta
from .models import UserSubscription, Subscription


def check_subscription(request):
    if request.user.is_authenticated:
        try:
            current_user = UserSubscription.objects.get(user=request.user)

            if current_user.expiry_date < datetime.now().date():  # Checking if the subscription is expired
                current_user.subscribed = False
                current_user.save()
                messages.error(request, "Your subscription is expired. Please get a new one")
            else:
                current_user.subscribed = True  # If not expired - make sure it's active
                current_user.save()

            if current_user.subscribed:
                return redirect('lessons')
        except UserSubscription.DoesNotExist:
            pass

    if request.user.is_superuser:  # Show all subscriptions to the admin (including disabled)
        subscriptions = Subscription.objects.all().order_by('duration')
    else:
        subscriptions = Subscription.objects.filter(is_active=True).order_by('duration')
    context = {
        'subscriptions': subscriptions,
    }
    return render(request, 'lessons/subscriptions.html', context)


def purchase_subscription(request, subscription_id):
    if request.method == 'POST' and request.user.is_authenticated:
        try:
            subscription = Subscription.objects.get(id=subscription_id)
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
            messages.success(request, "Subscription purchased successfully!")
            return redirect('lessons')
        except Subscription.DoesNotExist:
            messages.error(request, "Subscription not found")
            return redirect('your_error_url')
    return redirect('account_login')
def show_lessons(request):
    return render(request, 'lessons/lessons.html')