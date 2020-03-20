from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  related_name="profile")
    github_user = models.CharField(max_length=20, blank=True)
    github_streak = models.IntegerField(default=0)
    last_modified = models.DateTimeField(blank=True, null=True)

    # submit streak button, check github api, make an entry
    # displays entries for user on dash page

    def __str__(self):
        return f'{self.user.username} Profile'

