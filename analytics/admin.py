from django.contrib import admin
from .models import AnalyticsData, MonthlyStats

@admin.register(AnalyticsData)
class AnalyticsDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_sessions', 'total_reading_time', 'updated_at')
    search_fields = ('user__username',)

@admin.register(MonthlyStats)
class MonthlyStatsAdmin(admin.ModelAdmin):
    list_display = ('user', 'month', 'sessions_completed', 'best_streak')
    list_filter = ('month',)
    search_fields = ('user__username',)
