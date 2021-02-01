from django.db import models

# Create your models here.
class CheckersModel(models.Model):

    CHECK_MODES = (
        (1, "VALIDITY"),  # Respond with a valid ssl certificate
        (2, "HTTPOK"),  # Respond with http code 200
    )

    created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    modified = models.DateTimeField(auto_now=True, verbose_name="Date de modification")
    check = models.PositiveIntegerField(
        choices=CHECK_MODES,
        default=1,
        blank=False,
        null=False,
    )

    class Meta:
        abstract = False