from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import UserProfile

@login_required
def profile(request):
    """User profile and settings page"""
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        user_profile.display_name = request.POST.get('display_name', user_profile.display_name)
        user_profile.theme_preference = request.POST.get('theme_preference', user_profile.theme_preference)
        if 'profile_picture' in request.FILES:
            user_profile.profile_picture = request.FILES['profile_picture']
        user_profile.save()
        return redirect('profile')
    
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'pages/profile.html', context)

@login_required
def logout_view(request):
    """Logout user"""
    logout(request)
    return redirect('landing')
