# Generated by Django 3.0.4 on 2020-03-18 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_github_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='github_streak',
            field=models.IntegerField(default=0),
        ),
    ]
