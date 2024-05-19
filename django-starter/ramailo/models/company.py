from .base import BaseModel
from django.db import models

class Company(BaseModel):
    name = models.CharField(max_length=1024)
    company_id = models.CharField(max_length=255,  blank=True, null=True)
    api_key = models.CharField(max_length=255, blank=True, null=True)
    secret_key = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Companies"