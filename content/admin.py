from django.contrib import admin
from .models import Content

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'category', 'created_at')
    list_filter = ('content_type', 'category')
    search_fields = ('title', 'description')
