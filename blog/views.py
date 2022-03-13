from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Blog
from .forms import BlogForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def all_blog(request):
    """ To show all Blog"""
    blogs = Blog.objects.order_by('date_of_post')
    context = {'blogs':blogs}

    return render(request, 'all_blog.html', context)

def blog_detail(request, blog_id):
    """ show blog detail"""

    blogs = Blog.objects.all()
    blog = Blog.objects.get(id=blog_id)
    author = blog.author
    related_blogs = author.author_blogs.all()[:3]

    context = {'blog':blog, 'related_blogs': related_blogs, 'blogs':blogs}
    return render(request, 'blog_detail_view.html', context)

@login_required
def blog_create(request):
    """create blog"""

    if request.method == 'POST':
        form = BlogForm(data=request.POST)

        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user.author # set the current user as the author
            new_blog.save()

            return HttpResponseRedirect(reverse('bloggers-profile'))
    else:
        form = BlogForm()

    context = {'form':form, }
    return render(request, 'create_blog.html', context)

def blog_edit(request, blog_id):
    # to get the blog instance with 'blog_id' and set it to blog
    blog = Blog.objects.get(id=blog_id)

    if request.method == 'POST':
        form = BlogForm(instance=blog, data=request.POST) # populate the form with the instance of the pre-existing blog

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('bloggers-profile'))
    else:
        form = BlogForm(instance=blog)

    context = {'form':form, 'blog':blog}
    return render(request, 'blog_edit.html', context)


def blog_delete(request, blog_id):
    delete_blog = Blog.objects.get(id=blog_id)
    delete_blog.delete()
    return HttpResponseRedirect(reverse('bloggers-profile'))

