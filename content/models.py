from django.db import models

class Content(models.Model):
    """Content items like articles, videos, etc."""
    CONTENT_TYPE_CHOICES = [
        ('article', 'Article'),
        ('video', 'Video'),
        ('pdf', 'PDF'),
        ('resource', 'Resource'),
    ]

    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    url = models.URLField()
    category = models.CharField(max_length=50)
    thumbnail = models.URLField(blank=True)
    duration_minutes = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.content_type})"

    class Meta:
        ordering = ['-created_at']
