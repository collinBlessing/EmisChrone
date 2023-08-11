from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# register model ie user


class School_register(AbstractUser):
    def __str__(self):
        return self.email

    Userschoolname = models.CharField(max_length=100)
    institutionType = models.CharField(max_length=20)
