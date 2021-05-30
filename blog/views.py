from django.shortcuts import render

from .models import Blog, Post


def base_blog(request):
    #blog = Blog.objects.get(slug__iexact=slug)
    return render(request, 'blog/base_blog.html')

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', context={'blogs': blogs})

def blog_detail(request, slug):
    blog = Blog.objects.get(slug__iexact=slug)
    posts = Post.objects.filter(blog=blog)
    ordered_posts = posts.order_by('-create_time')[:3]
    return render(request, 'blog/blog_detail.html', context={'blog': blog, 'posts': ordered_posts})
