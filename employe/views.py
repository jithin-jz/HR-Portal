from django.shortcuts import render, get_object_or_404
from app.models import UserProfile


def employe(request):
    profiles = UserProfile.objects.all().order_by('-id')
    context = {
        'profiles': profiles,
        'total_employees': profiles.count(),
    }
    return render(request, 'employe.html', context)

# View for displaying a specific user's profile
def profile_view(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'profile.html', {'user_profile': user_profile})

