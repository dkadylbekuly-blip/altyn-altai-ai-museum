from django.db import models
from django.utils.text import slugify

class Mineral(models.Model):
    CATEGORY_CHOICES = [
        ("mineral", "Минерал"),
        ("rock", "Горная порода"),
        ("glass", "Вулканическое стекло"),
        ("gem", "Драгоценный камень"),
    ]

    slug = models.SlugField(unique=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    slug = models.SlugField(
        max_length=120,
        unique=True,
        verbose_name="Ключ модели",
    )

    title = models.CharField(
        max_length=200,
        verbose_name="Название",
    )

    formula = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Формула",
    )

    color = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Цвет",
    )

    hardness = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Твёрдость",
    )

    origin = models.TextField(
        blank=True,
        verbose_name="Происхождение",
    )

    usage = models.TextField(
        blank=True,
        verbose_name="Применение",
    )

    description = models.TextField(
        blank=True,
        verbose_name="Описание",
    )

    facts = models.JSONField(
        default=list,
        blank=True,
        verbose_name="Интересные факты",
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="mineral",
        verbose_name="Категория",
    )

    image = models.ImageField(
        upload_to="minerals/",
        blank=True,
        null=True,
        verbose_name="Фото",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Минерал"
        verbose_name_plural = "Минералы"
        ordering = ["title"]

    def __str__(self):
        return self.title
    
class MineralI18n(models.Model):
    LANG_CHOICES = [
        ("kk", "Қазақша"),
        ("ru", "Русский"),
        ("en", "English"),
    ]

    raw_slug = models.SlugField(
        max_length=150,
        verbose_name="ML класс (raw slug)",
    )
    canonical_key = models.SlugField(
        max_length=150,
        verbose_name="Негізгі ғылыми кілт",
    )
    lang = models.CharField(
        max_length=2,
        choices=LANG_CHOICES,
        verbose_name="Тіл",
    )

    title = models.CharField(max_length=255, verbose_name="Атауы")
    color = models.CharField(max_length=255, blank=True, verbose_name="Түсі / Цвет / Colour")
    formula = models.CharField(max_length=255, blank=True, verbose_name="Формула")
    luster = models.CharField(max_length=255, blank=True, verbose_name="Жылтырлығы / Блеск / Luster")
    mohs_scale = models.CharField(max_length=100, blank=True, verbose_name="Қаттылығы / Mohs scale")
    cleavage = models.CharField(max_length=255, blank=True, verbose_name="Жіктілігі / Спайность / Cleavage")
    fracture = models.CharField(max_length=255, blank=True, verbose_name="Сынықтылығы / Излом / Fracture")
    crystal_system = models.CharField(max_length=255, blank=True, verbose_name="Сингониясы / Crystal system")

    description = models.TextField(blank=True, verbose_name="Түсіндірмесі / Описание / Description")
    origin = models.TextField(blank=True, verbose_name="Шығу тегі / Происхождение / Origin")
    uses = models.TextField(blank=True, verbose_name="Пайдалануы / Применение / Uses")
    deposits = models.TextField(blank=True, verbose_name="Кенорындары / Месторождения / Deposits")
    interesting_facts = models.JSONField(default=list, blank=True, verbose_name="Қызықты факттер")

    image = models.ImageField(upload_to="minerals_i18n/", blank=True, null=True)
    is_verified = models.BooleanField(default=False, verbose_name="Тексерілген бе")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Көптілді минерал"
        verbose_name_plural = "Көптілді минералдар"
        unique_together = ("raw_slug", "lang")
        ordering = ["lang", "title"]

    def __str__(self):
        return f"{self.get_lang_display()} | {self.title} | {self.raw_slug}"