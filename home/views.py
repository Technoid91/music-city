from django.shortcuts import render

from products.models import Product
from lessons.models import Subscription


from django.core.mail import get_connection, EmailMessage
from django.conf import settings

def index(request):
    """ Render the home page with products with special prices """

    subject = "Your Subject"
    body = "This is a test email."
    recipient_email = "technoid91@gmail.com"

    connection = get_connection(
        backend='django.core.mail.backends.smtp.EmailBackend',
        host=settings.EMAIL_HOST,
        port=settings.EMAIL_PORT,
        username=settings.EMAIL_HOST_USER,
        password=settings.EMAIL_HOST_PASSWORD,
        use_tls=settings.EMAIL_USE_TLS,
    )

    email = EmailMessage(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [recipient_email],
        connection=connection
    )

    try:
        email.send()
        print("Test email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

    products = Product.objects.filter(old_price__isnull=False)
    products_amount = products.count()
    if products_amount > 3:
        products = Product.objects.filter(old_price__isnull=False).order_by('?')[:3]
    context = {
        'products': products,
    }
    return render(request, "home/index.html", context)
