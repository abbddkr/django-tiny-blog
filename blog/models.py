from django.db import models
from django.contrib.auth.models import User
from martor.models import MartorField
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Post(models.Model):

    TYPE_CHOICES = (
        ('page', 'Page'),
        ('post', 'Post'),
    )

    STATUS_CHOICES = (
            ('published', 'Published'),
            ('draft', 'Draft'),
            ('review', 'Under Review'),
        )


    title = models.CharField(max_length=180)
    short_desc = models.CharField(max_length=250)
    content = MartorField()
    thumbnail = models.ImageField(upload_to ='uploads/', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='post')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='review')
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.title


