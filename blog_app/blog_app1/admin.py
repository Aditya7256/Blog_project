from django.contrib import admin
from .models import Blog
# Register your models here.
@admin.register(Blog)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']
