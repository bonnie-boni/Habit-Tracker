from django.contrib import admin
from .models import Habit, Session

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'habit_type', 'category', 'current_streak', 'is_active')
    list_filter = ('habit_type', 'category', 'is_active')
    search_fields = ('user__username', 'name')

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('habit', 'started_at', 'completed', 'progress_percentage')
    list_filter = ('completed', 'started_at')
    search_fields = ('habit__name',)
