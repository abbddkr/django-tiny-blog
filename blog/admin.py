from django.contrib import admin
from django.db import models
from .models import Post
from .models import Category
from martor.widgets import AdminMartorWidget

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    override_fields = {
        models.TextField: {'widget', AdminMartorWidget}
    }

admin.site.register(Post)
admin.site.register(Category)
