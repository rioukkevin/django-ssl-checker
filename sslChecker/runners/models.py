from django.db import models
from checkers.models import CheckersModel
from websites.models import WebsitesModel

# Create your models here.
class RunnersModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    modified = models.DateTimeField(auto_now=True, verbose_name="Date de modification")
    isSuccess = models.BooleanField(default=False, blank=False)
    websites = models.ForeignKey(
        WebsitesModel,
        on_delete=models.CASCADE,
        unique=False,
        null=True,
    )
    # Many to Many exemple md
    checkers = models.ManyToManyField(
        CheckersModel,
        blank=True,
    )

    def __str__(self):
        return str(self.websites.name)

    class Meta:
        abstract = False