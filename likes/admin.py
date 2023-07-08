from django.contrib import admin
from django.db import models
from .models import Like


@admin.register(Like)
class LikeAdmin(models.ModelAdmin):
    list_display = ('owner', 'poem', 'created_at')
    search_fields = ('owner', 'poem',)
    list_filter = ('owner', 'poem',)
