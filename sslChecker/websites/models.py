from django.db import models

# Create your models here.
class WebsitesModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    modified = models.DateTimeField(auto_now=True, verbose_name="Date de modification")
    name = models.TextField(
        primary_key=True,
        verbose_name="Nom du site à inspecter",
        blank=False,
    )
    url = models.TextField(
        primary_key=False,
        verbose_name="Url du site à inspecter",
        blank=False,
        default="https://google.com",
    )

    class Meta:
        abstract = False
        ordering = ("-name",)
