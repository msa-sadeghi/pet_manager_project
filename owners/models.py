from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Owner(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="owner_profile",
        verbose_name="کاربر",
    )
    phone = models.CharField(max_length=15, verbose_name="شماره تلفن")
    address = models.TextField(verbose_name="آدرس", blank=True)
    city = models.CharField(max_length=100, verbose_name="شهر", blank=True)
    national_id = models.CharField(
        max_length=10, verbose_name="کد ملی", unique=True, blank=True
    )
    profile_picture = models.ImageField(
        upload_to="owners/", verbose_name="تصویر پروفایل", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت نام")

    class Meta:
        verbose_name = "صاحب حیوان"
        verbose_name_plural = "صاحبان حیوانات"
        ordering = ["user__last_name"]

    def __str__(self):
        return f"{self.user.username} salaam"
