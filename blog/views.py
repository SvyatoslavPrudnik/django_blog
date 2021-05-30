from django.shortcuts import render


def base_blog(request):
    #blog = Blog.objects.get(slug__iexact=slug)
    return render(request, 'blog/base_blog.html')
