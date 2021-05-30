from django.urls import path

from .views import base_blog


urlpatterns = [
    path('', base_blog, name='base_blog_url'),
]