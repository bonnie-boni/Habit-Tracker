from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import AnalyticsData, MonthlyStats

@login_required
def analytics_dashboard(request):
    """Display user analytics and progress"""
    analytics, created = AnalyticsData.objects.get_or_create(user=request.user)
    monthly_stats = request.user.monthly_stats.all()[:12]  # Last 12 months
    
    context = {
        'analytics': analytics,
        'monthly_stats': monthly_stats,
    }
    return render(request, 'pages/analytics.html', context)
