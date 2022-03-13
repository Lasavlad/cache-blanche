from unicodedata import name
from django.urls import path
from .views import all_blog, blog_detail, blog_create, blog_delete, blog_edit

urlpatterns = [
    path('all-blog/', all_blog, name='all-blog'),
    path('blog/<int:blog_id>', blog_detail, name='blog-detail'),
    path('create/', blog_create, name='create-blog'),
    path('edit/<int:blog_id>', blog_edit, name='blog-edit'),
    path('delete/<int:blog_id>', blog_delete, name='blog-delete' ),
]