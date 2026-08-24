from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True)
    locations = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"profile {self.user.username}"

    
