from re import template
from django.shortcuts import render
from django.views.generic import TemplateView

class Frontpage(TemplateView):
    template_name = 'frontpage.html'


# Create your views here.
