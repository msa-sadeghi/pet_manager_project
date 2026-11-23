from django.db import models
from pets.models import Pet
from datetime import date


class VisitType(models.TextChoices):
    CHECKUP = "checkup", "معاینه عمومی"
    EMERGENCY = "emergency", "اورژانس"
    VACCINATION = "vaccination", "واکسیناسیون"
    SURGERY = "surgery", "جراحی"
    FOLLOWUP = "followup", "پیگیری"


class Vaccine(models.Model):
    pet = models.ForeignKey(
        Pet, on_delete=models.CASCADE, related_name="vaccines", verbose_name="حیوان"
    )
    name = models.CharField(max_length=100, verbose_name="نام واکسن")
    date_given = models.DateField(verbose_name="تاریخ تزریق")
    next_due = models.DateField(blank=True, null=True, verbose_name="نوبت بعدی")
    batch_number = models.CharField(max_length=50, blank=True, verbose_name="شماره سری")
    administered_by = models.CharField(
        max_length=100, blank=True, verbose_name="تزریق کننده"
    )
    notes = models.TextField(blank=True, verbose_name="یادداشت")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "واکسن"
        verbose_name_plural = "واکسن‌ها"
        ordering = ["-date_given"]

    def __str__(self):
        return f"{self.name} - {self.pet.name} ({self.date_given})"

    def is_overdue(self):
        if not self.next_due:
            return False
        return self.next_due < date.today()

    def days_until_due(self):
        if not self.next_due:
            return None
        delta = self.next_due - date.today()
        return delta.days


class VetVisit(models.Model):
    pet = models.ForeignKey(
        Pet, on_delete=models.CASCADE, related_name="visits", verbose_name="حیوان"
    )
    visit_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ویزیت")
    visit_type = models.CharField(
        max_length=20,
        choices=VisitType.choices,
        default=VisitType.CHECKUP,
        verbose_name="نوع ویزیت",
    )
    vet_name = models.CharField(max_length=100, blank=True, verbose_name="نام دامپزشک")
    weight_at_visit = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        verbose_name="وزن هنگام ویزیت",
    )
    diagnosis = models.TextField(blank=True, verbose_name="تشخیص")
    treatment = models.TextField(blank=True, verbose_name="درمان")
    prescribed_medicines = models.TextField(blank=True, verbose_name="داروهای تجویزی")
    cost = models.DecimalField(
        max_digits=10, decimal_places=0, default=0, verbose_name="هزینه (تومان)"
    )
    next_appointment = models.DateTimeField(
        blank=True, null=True, verbose_name="نوبت بعدی"
    )
    notes = models.TextField(blank=True, verbose_name="یادداشت")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "ویزیت"
        verbose_name_plural = "ویزیت‌ها"
        ordering = ["-visit_date"]

    def __str__(self):
        visit_type_display = dict(VisitType.choices).get(
            self.visit_type, self.visit_type
        )
        return f"{self.pet.name} | {visit_type_display} | {self.visit_date.strftime('%Y-%m-%d')}"
