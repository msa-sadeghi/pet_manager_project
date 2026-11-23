from django.db import models
from owners.models import Owner
from datetime import date


class Pet(models.Model):

    class Species(models.TextChoices):
        DOG = "dog", "سگ"
        CAT = "cat", "گربه"
        BIRD = "bird", "پرنده"
        RABBIT = "rabbit", "خرگوش"
        FISH = "fish", "ماهی"
        OTHER = "other", "سایر"

    class Gender(models.TextChoices):
        MALE = "male", "نر"
        FEMALE = "female", "ماده"
        UNKNOWN = "unknown", "نامشخص"

    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        related_name="pets",
        verbose_name="صاحب"
    )
    name = models.CharField(max_length=100, verbose_name="نام")
    species = models.CharField(
        max_length=20,
        choices=Species.choices,
        verbose_name="گونه"
    )
    breed = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="نژاد"
    )
    gender = models.CharField(
        max_length=20,
        choices=Gender.choices,
        verbose_name="جنسیت"
    )
    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="تاریخ تولد"
    )
    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="وزن"
    )
    color = models.CharField(
        max_length=50,
        verbose_name="رنگ"
    )
    photo = models.ImageField(
        upload_to="pets/photos/",
        blank=True,
        null=True,
        verbose_name="عکس حیوان"
    )
    microchip_id = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        verbose_name="کد میکروچیپ"
    )
    is_neutered = models.BooleanField(
        default=False,
        verbose_name="عقیم شده؟"
    )
    notes = models.TextField(
        blank=True,
        verbose_name="یادداشت‌ها"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="ایجاد"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین تغییر"
    )

    def __str__(self):
        return f"{self.name} ({self.get_species_display()}) - {self.owner}"

    def get_age(self):
        if not self.birth_date:
            return None
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )

    def get_age_display(self):
        age = self.get_age()
        if age is None:
            return "نامشخص"
        if age < 1:
            return "کمتر از یک سال"
        return f"{age} سال"

    class Meta:
        verbose_name = "حیوان خانگی"
        verbose_name_plural = "حیوانات خانگی"
        ordering = ["name"]