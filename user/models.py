from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    profile_bio = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.user.username

