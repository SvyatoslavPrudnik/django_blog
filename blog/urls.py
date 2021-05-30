from django.urls import path

from .views import base_blog, blog_list, blog_detail


urlpatterns = [
    path('', base_blog, name='base_blog_url'),
    path('blogs/', blog_list, name='blog_list_url'),
    path('<str:slug>/', blog_detail, name='blog_detail_url'),
]