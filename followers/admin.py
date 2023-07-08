from django.contrib import admin
from django.db import models
from .models import Follower


@admin.register(Follower)
class AdminFollower(admin.ModelAdmin):
    list_display = ['owner', 'followed', 'created_at']
    search_fields = ['owner', 'followed']
    list_filter = ['owner', 'followed']
