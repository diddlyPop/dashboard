from django.db import models

# Create your models here.


class Mark(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
