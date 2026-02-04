from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('user', 'habit', 'event_type', 'created_at')
    list_filter = ('event_type', 'created_at')
    search_fields = ('user__username', 'habit__name')
    date_hierarchy = 'created_at'
