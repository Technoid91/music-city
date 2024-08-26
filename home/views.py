from django.shortcuts import render

from products.models import Product
from lessons.models import Subscription


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.conf import settings




def index(request):
    """ Render the home page with products with special prices """

    subject = "Your Subject"
    body = "This is a test email."
    recipient_email = "technoid91@gmail.com"

    # Создаем сообщение
    msg = MIMEMultipart()
    msg['From'] = settings.EMAIL_HOST_USER
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Устанавливаем соединение с сервером
        server = smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT)
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        # Отправляем письмо
        server.sendmail(settings.EMAIL_HOST_USER, recipient_email, msg.as_string())
        server.quit()
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
