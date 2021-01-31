from django.db import models

# Create your models here.
class RunnersModel(models.Model):

    CHECK_MODES = (
        (1, "VALIDITY"),  # Respond with a valid ssl certificate
        (2, "HTTPOK"),  # Respond with http code 200
    )

    created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    modified = models.DateTimeField(auto_now=True, verbose_name="Date de modification")
    isSuccess = models.BooleanField(default=False, blank=False)

    class Meta:
        abstract = False