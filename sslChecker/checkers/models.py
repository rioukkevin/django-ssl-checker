from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CheckersModel(models.Model):
    class CHECKS(models.TextChoices):
        VALIDITY = "VALIDITY", _("Validity")
        HTTPOK = "HTTPOK", _("HTTPok")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    modified = models.DateTimeField(auto_now=True, verbose_name="Date de modification")
    check = models.TextField(
        choices=CHECKS.choices,
        default=CHECKS.VALIDITY,
        blank=False,
        null=False,
    )

    def __str__(self):
        return str(self.check)

    class Meta:
        abstract = False