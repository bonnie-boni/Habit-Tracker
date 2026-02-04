from django.db import models
from django.contrib.auth.models import User

class Habit(models.Model):
    """User's habit record"""
    HABIT_TYPE_CHOICES = [
        ('build', 'Build a Habit'),
        ('drop', 'Drop a Habit'),
    ]
    
    CATEGORY_CHOICES = [
        ('reading', 'Reading'),
        ('fitness', 'Fitness'),
        ('meditation', 'Meditation'),
        ('learning', 'Learning'),
        ('addiction', 'Addiction Support'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')
    habit_type = models.CharField(max_length=10, choices=HABIT_TYPE_CHOICES)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    current_streak = models.IntegerField(default=0)
    best_streak = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"

    class Meta:
        ordering = ['-updated_at']


class Session(models.Model):
    """Temporary session for reading or activity"""
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='sessions')
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    progress_percentage = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    content_id = models.CharField(max_length=255, blank=True)  # Reference to content item

    def __str__(self):
        return f"Session {self.id} - {self.habit.name}"
