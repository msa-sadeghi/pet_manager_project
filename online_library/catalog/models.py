from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField("نام", max_length=100)
    last_name = models.CharField("نام خانوادگی", max_length=100)
    slug = models.SlugField("اسلاگ", unique=True)
    bio = models.TextField("زندگی نامه", blank=True)
    birth_date = models.DateField("تاریخ تولد", null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "نویسنده"
        verbose_name_plural = "نویسندگان"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Publisher(models.Model):
    name = models.CharField("نام", max_length=150, unique=True)
    city = models.CharField("شهر", max_length=100, blank=True)
    website = models.URLField("وب سایت", blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "ناشر"
        verbose_name_plural = "ناشران"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField("نام", max_length=150, unique=True)
    slug = models.SlugField("اسلاگ")
    description = models.TextField("توضیح", blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.name


isbn_validator = RegexValidator(regex=r"^\d{13}$", message="ISBN must be 13 digits")


class Book(models.Model):
    class Language(models.TextChoices):
        PERSIAN = "fa", "فارسی"
        ENGLISH = "en", "انگلیسی"
        ARABIC = "ar", "عربی"

    title = models.CharField("عنوان", max_length=200, db_index=True)
    slug = models.SlugField("اسلاگ", unique=True)
    isbn = models.CharField(
        "شابک", max_length=13, unique=True, validators=[isbn_validator], help_text="13 رقم بدون تیره"
    )
    description = models.TextField("توضیحات", blank=True)
    authors = models.ManyToManyField(Author, related_name="books", verbose_name="نویسندگان")
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, related_name="books", verbose_name="ناشر")
    Category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="books", verbose_name="دسته بندی"
    )
    published_year = models.PositiveSmallIntegerField(
        "سال انتشار", validators=[MinValueValidator(1000), MaxValueValidator(2100)]
    )

    language = models.CharField("زبان", max_length=2, choices=Language.choices, default=Language.PERSIAN)

    total_copies = models.PositiveSmallIntegerField("تعداد کل نسخه ها", default=1)
    available_copies = models.PositiveSmallIntegerField("نسخه های موجود", default=1)
    is_active = models.BooleanField("فعال", default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب ها"
        indexes = [models.Index(fields=["published_year", "language"], name="book_year_lang_idx")]
        constraints = [
            models.UniqueConstraint(fields=["title", "publisher"], name="unique_title_per_publisher"),
            models.CheckConstraint(
                condition=models.Q(available_copies__lte=models.F("total_copies")), name="available_lte_total"
            ),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("catalog:book_detail", kwargs={"pk": self.slug})
