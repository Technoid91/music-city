from django.contrib.auth.models import User
from django.db import models


class Subscription(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    promotional_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class UserSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=False)
    subscription_name = models.CharField(max_length=40)
    start_date = models.DateField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Subscribed User"
        verbose_name_plural = "Subscribed Users"
