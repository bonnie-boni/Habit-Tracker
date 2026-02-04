from django.db import models
from django.contrib.auth.models import User

class AnalyticsData(models.Model):
    """Aggregated analytics for user habits"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='analytics')
    total_sessions = models.IntegerField(default=0)
    total_reading_time = models.IntegerField(default=0)  # in minutes
    total_resistances = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Analytics for {self.user.username}"


class MonthlyStats(models.Model):
    """Monthly performance tracking"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='monthly_stats')
    month = models.DateField()  # First day of month
    sessions_completed = models.IntegerField(default=0)
    best_streak = models.IntegerField(default=0)
    total_minutes = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'month')
        ordering = ['-month']
