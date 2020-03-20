from django import forms
from django.contrib.auth.models import User


class StreakUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['github_streak']

