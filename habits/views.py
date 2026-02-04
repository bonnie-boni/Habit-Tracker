from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Habit, Session

@login_required
def dashboard(request):
    """Main dashboard view"""
    try:
        habit = request.user.habits.filter(is_active=True).first()
    except:
        habit = None
    
    if not habit:
        return redirect('onboarding')
    
    context = {
        'habit': habit,
        'current_streak': habit.current_streak,
        'best_streak': habit.best_streak,
    }
    
    if habit.habit_type == 'build':
        return render(request, 'pages/dashboard_build.html', context)
    else:
        return render(request, 'pages/dashboard_drop.html', context)


@login_required
def onboarding(request):
    """Habit selection and setup"""
    if request.method == 'POST':
        habit_type = request.POST.get('habit_type')
        category = request.POST.get('category')
        name = request.POST.get('name')
        
        habit = Habit.objects.create(
            user=request.user,
            habit_type=habit_type,
            category=category,
            name=name,
        )
        return redirect('dashboard')
    
    context = {
        'habit_types': Habit.HABIT_TYPE_CHOICES,
        'categories': Habit.CATEGORY_CHOICES,
    }
    return render(request, 'pages/onboarding.html', context)


@login_required
def read_page(request):
    """E-reader page for reading content"""
    habit = request.user.habits.filter(habit_type='build', category='reading', is_active=True).first()
    if not habit:
        return redirect('dashboard')
    
    session = habit.sessions.filter(completed=False).last()
    if not session:
        session = Session.objects.create(habit=habit)
    
    context = {
        'habit': habit,
        'session': session,
    }
    return render(request, 'pages/read_page.html', context)


@login_required
def video_watch(request):
    """Video watch page for habit dropping"""
    habit = request.user.habits.filter(habit_type='drop', is_active=True).first()
    if not habit:
        return redirect('dashboard')
    
    context = {
        'habit': habit,
    }
    return render(request, 'pages/video_watch.html', context)
