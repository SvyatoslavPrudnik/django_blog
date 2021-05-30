from django.shortcuts import render

from .models import Blog


def base_blog(request):
    #blog = Blog.objects.get(slug__iexact=slug)
    return render(request, 'blog/base_blog.html')

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', context={'blogs': blogs})
