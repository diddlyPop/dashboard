from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import Profile
from .funcs import update_streaks
from django.contrib import messages
import datetime
import requests


def home(request):
    """
    Front Page view
    :param request:
    :return:
    """
    profiles = Profile.objects.all().order_by("github_streak")
    context = {
        'profiles': profiles
    }
    return render(request, 'index.html', context)


@login_required
def dash(request):
    """
    Dashboard view - will load and serve all widgets on dash
    Currently displays streak widget
    :param request: if 'request' is a POST, update the streak widget
    :return: 'dash.html' with widget contexts
    """
    # Load the user's profile and relevant information
    profile = Profile.objects.get(user=request.user)
    streaks = profile.github_streak
    github_user = profile.github_user
    last_modified = profile.last_modified

    # Send streak color as context to dash template. Sets bg_color of streak widget
    streak_color = "red"
    if last_modified is not None and last_modified.date() == datetime.date.today():
        streak_color = "green"

    # User is attempting to update their streak
    if request.method == "POST":
        if 'streak-update-form' in request.POST:
            # 'result' tells if we should update streak
            # There are various related messages to display to the user retrieved from the function
            result, message = update_streaks(github_user, last_modified)
            # We will update the streak
            if result:
                # Logic for if user missed a streak
                if message == "Reset":
                    profile.github_streak = 1
                    message = "You lost your streak. We're starting a new one."
                # Increment streak
                else:
                    profile.github_streak += 1
                # Update the last streak time, and save the profile
                profile.last_modified = datetime.date.today()
                profile.save()
                # Reload streaks for context
                streaks = profile.github_streak
            # Display user's personalized message feedback
            messages.success(request, message)
    context = {'streaks': streaks, 'g_user': github_user, 'range': range(streaks), 'completed_streak_today': streak_color}
    return render(request, 'dash.html', context)
