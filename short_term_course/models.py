from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ShortTermCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True)
    title = models.CharField(max_length=255, unique=True, blank = True, null = True)
    subtitle = models.CharField(max_length=255, blank = True, null = True)
    amount = models.CharField(max_length=255, blank = True, null = True)
    amount_text = models.CharField(max_length=255, blank = True, null = True)
    status = models.CharField(max_length=255, blank = True, null = True)
    images = models.ImageField(default=True, upload_to='photos/courses', blank=True, null=True)