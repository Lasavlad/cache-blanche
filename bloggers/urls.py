from unicodedata import name
from django.urls import path
from .views import SignUp, bloggers_profile, edit_profile

urlpatterns = [
    path('signup/', SignUp.as_view(), name='sign-up'),
    path('profile/', bloggers_profile, name='bloggers-profile'),
    path('edit-profie/', edit_profile, name="edit-profile")
]