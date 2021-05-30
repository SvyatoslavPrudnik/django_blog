from django.urls import path

from .views import base_blog, blog_list


urlpatterns = [
    path('', base_blog, name='base_blog_url'),
    path('blogs/', blog_list, name='blog_list_url'),
]