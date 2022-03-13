from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomAuthorModel(AbstractUser):
    about_self = models.TextField(max_length=1000)
    date_of_registration = models.DateField(auto_now_add=True)

