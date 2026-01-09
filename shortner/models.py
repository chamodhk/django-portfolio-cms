from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse


class ShortURL(models.Model):
    code = models.SlugField(
        max_length=50,
        unique=True,
        help_text="The short code, for example: github",
    )
    destination_url = models.URLField(max_length=2048)
    title = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    click_count = models.PositiveBigIntegerField(default=0, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Short URL"
        verbose_name_plural = "Short URLs"

    def __str__(self):
        return self.title or self.code

    def get_absolute_url(self):
        return reverse("shortener:redirect", kwargs={"code": self.code})