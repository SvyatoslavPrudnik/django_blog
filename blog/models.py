from django.db import models


class Blog(models.Model):
    CHOICES = [
        ('VG', 'Videogames'),
        ('F', 'Films'),
        ('P', 'Politics'),
        ('T', 'Travel'),
    ]
    title = models.CharField(max_length=150)
    description = models.TextField()
    blog_topic = models.CharField(max_length=300, choices = CHOICES)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=150, unique=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.create_time

class Tag(models.Model):
    title = models.CharField(max_length=150)
    frequency = models.IntegerField()
    slug = models.SlugField(max_length=150, unique=True)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.title

