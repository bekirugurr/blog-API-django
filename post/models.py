from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from django.contrib.auth.models import User


def unique_slugify(instance, slug):
    model = instance.__class__
    unique_slug = slug
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = slug + get_random_string(length=4)
    return unique_slug

class Category(models.Model):
    CATEGORY = (
    ('I' , 'IT'),
    ('B' , 'Book'),
    ('M' , 'Movie'),
    ('L' , 'Life'),
    ('P' , 'Personal'),
    )
    category = models.CharField(max_length=50, choices=CATEGORY, default='L')

    def __str__(self):
        return f'{self.category}'


class Post(models.Model): 
    STATUS = (
    ('P' , 'Published'),
    ('D' , 'Draft')
    )
    title = models.CharField(max_length=50)
    content = models.TextField()
    post_pic = models.ImageField(upload_to='post_pics', blank=True,  null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS, default='D')
    slug = models.SlugField(null=False, blank=True, editable=False)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=17)

    def __str__(self):
        return f'{self.title}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, slugify(self.title))
        super().save(*args, **kwargs)


class Comment(models.Model):
    content = models.TextField(max_length=300)
    date_stamp = models.DateTimeField(auto_now_add=True)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name='comments')


class Like(models.Model):
    who_liked = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name='likes')

class PostView(models.Model):
    who_viewed = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name='views')


