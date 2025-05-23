from django.db import models
from django.utils.text import slugify
from instruments.models import Specialty

# Create your models here.
class AnatomySystem(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class AnatomyMain(models.Model):
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, blank=True, null=True)
    system = models.ForeignKey(AnatomySystem, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    model_embed_code1 = models.TextField(blank=True, null=True)
    model_embed_code2 = models.TextField(blank=True, null=True)
    model_embed_code3 = models.TextField(blank=True, null=True)
    model_embed_code4 = models.TextField(blank=True, null=True)

    description1 = models.TextField(blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)
    description3 = models.TextField(blank=True, null=True)
    description4 = models.TextField(blank=True, null=True)

    def get_embed_codes(self):
        return [code for code in [self.model_embed_code1, self.model_embed_code2, self.model_embed_code3, self.model_embed_code4] if code]
    
    def get_descriptions(self):
        return [desc for desc in [self.description1, self.description2, self.description3, self.description4] if desc]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(str(self.system))
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.system)
    

