from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True)
    locations = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"profile {self.user.username}"


class CustomUser(AbstractUser):

    def avatar_upload_path(instance, filename):
        return f"avatars/{instance.username}/{filename}"

    phone = models.CharField(max_length=15, verbose_name="تلفن")
    bio = models.TextField()
    avatar = models.ImageField(upload_to=avatar_upload_path, blank=True, null=True, verbose_name="تصویر پروفایل")
    website = models.URLField(blank=True, verbose_name="وب سایت")
    birth_date = models.DateField(null=True, blank=True, verbose_name="تاریخ تولد")

    def __str__(self):
        return self.username

    def get_full_name(self):
        full = super().get_full_name()
        return full if full else self.username

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return f"/static/accounts/img/default_avatar.png"
