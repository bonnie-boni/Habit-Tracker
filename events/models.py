from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    """Event tracking (source of truth)"""
    EVENT_TYPE_CHOICES = [
        ('read', 'Read'),
        ('blocked', 'Blocked'),
        ('resisted', 'Resisted'),
        ('completed', 'Completed'),
        ('started', 'Started'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    habit = models.ForeignKey('habits.Habit', on_delete=models.CASCADE, related_name='events')
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES)
    data = models.JSONField(default=dict, blank=True)  # Additional event data
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event_type} - {self.created_at}"

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', '-created_at']),
            models.Index(fields=['habit', '-created_at']),
        ]
