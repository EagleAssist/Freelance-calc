from django.db import models

from django.db import models


class User():
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    # You may want to use a better field for storing passwords, such as PasswordField
    # (from Django 3.1+), or use a third-party package like django-cryptography.

    def __str__(self):
        return self.username