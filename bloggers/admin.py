from django.contrib import admin
from .models import Author
from .forms import CustomAuthorCreationForm, CustomAuthorChangeForm
from django.contrib.auth.admin import UserAdmin
from core.models import CustomAuthorModel

class CustomAuthorAdmin(UserAdmin):
    add_form = CustomAuthorCreationForm
    form = CustomAuthorChangeForm
    model = CustomAuthorModel
    list_display = ['username', 'first_name', 'last_name', 'email']

admin.site.register(CustomAuthorModel, CustomAuthorAdmin)
admin.site.register(Author)

# Register your models here.
