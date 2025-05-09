from django.db import models
from django.utils.text import slugify
from instruments.models import Specialty

# Create your models here.

class AnatomyMain(models.Model):
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, blank=True, null=True)
    system = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.system)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.system} - {self.specialty}"
