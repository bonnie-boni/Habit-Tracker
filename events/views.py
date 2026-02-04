from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Event

@login_required
def event_log(request):
    """View recent events"""
    events = request.user.events.all()[:100]  # Last 100 events
    
    context = {
        'events': events,
    }
    return render(request, 'pages/event_log.html', context)
