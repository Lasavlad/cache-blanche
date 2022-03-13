import numbers
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from .forms import CustomAuthorCreationForm
from core.models import CustomAuthorModel
from django.views.generic import CreateView
from .models import Author
from blog.models import Blog
from django.contrib.auth.decorators import login_required

class SignUp(CreateView):
    form_class = CustomAuthorCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def bloggers_profile(request):
    author = request.user.author
    blogs = author.author_blogs.all()
    number_of_blog = blogs.all().count()

    context = {'author':author, 'blogs':blogs, 'number_of_blog':number_of_blog}
    return render(request, 'bloggers_profile.html', context)

@login_required
def edit_profile(request):
    author = request.user.author

    if request.method == 'POST':
        name = request.POST.get('first_name', '')
        email = request.POST.get('email', '')

        if name:
            author.created_by.email = email # user field email
            author.created_by.save()

            author.username = name
            author.save()

            return HttpResponseRedirect(reverse('bloggers-profile'))

    return render(request, 'edit_profile.html', {'author':author})