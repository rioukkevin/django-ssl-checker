from django.db import models
from runners.models import RunnersModel

# Create your models here.
class WebsitesModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    modified = models.DateTimeField(auto_now=True, verbose_name="Date de modification")
    name = models.TextField(
        primary_key=True,
        verbose_name="Nom du site à inspecter",
        blank=False,
        editable=False,
    )
    url = models.TextField(
        primary_key=False,
        verbose_name="Url du site à inspecter",
        blank=False,
        editable=False,
        default="https://google.com",
    )
    runner = models.OneToOneField(
        RunnersModel,
        on_delete=models.CASCADE,
        blank=False,
        null=True,
    )

    class Meta:
        abstract = False
        ordering = ("-name",)
