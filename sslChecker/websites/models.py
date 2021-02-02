from django.db import models

# Create your models here.
class WebsitesModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    modified = models.DateTimeField(auto_now=True, verbose_name="Date de modification")
    name = models.CharField(
        primary_key=False,
        max_length=200,
        verbose_name="Nom du site à inspecter",
        blank=False,
    )
    url = models.CharField(
        primary_key=False,
        max_length=2000,
        verbose_name="Url du site à inspecter",
        blank=False,
        default="https://google.com",
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        abstract = False
        ordering = ("-name",)
