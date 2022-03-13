
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from core.models import CustomAuthorModel

class CustomAuthorCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomAuthorModel
        fields = ('username', 'first_name', 'last_name', 'email', 'about_self')

class CustomAuthorChangeForm(UserChangeForm):
    class Meta:
        model = CustomAuthorModel
        fields = ('username', 'first_name', 'last_name', 'email', 'about_self')


