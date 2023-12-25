from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import News, Comment, Category

admin.site.register(News)
admin.site.register(Comment)
admin.site.register(Category)
