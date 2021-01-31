from django.db import models
from runners.models import RunnersModel

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
        default=None,
        blank=False,
        null=False,
    )
    runner = models.OneToOneField(
        RunnersModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = False