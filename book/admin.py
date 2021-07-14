from django.contrib import admin
from .models import Category, Photo

# Register your models here.
admin.site.register(Photo)
admin.site.register(Category)