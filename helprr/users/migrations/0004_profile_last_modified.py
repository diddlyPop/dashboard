# Generated by Django 3.0.4 on 2020-03-18 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_github_streak'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
