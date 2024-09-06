from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class NewsSubscriber(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email