from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """Extended user profile for Habit Tracker"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    display_name = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    theme_preference = models.CharField(
        max_length=10,
        choices=[('dark', 'Dark'), ('light', 'Light')],
        default='dark'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.display_name}"
