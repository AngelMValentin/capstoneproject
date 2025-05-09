from django.db import models
import random
from django.utils.text import slugify

# Create your models here.

class InstrumentType(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Instrument(models.Model):
    name = models.CharField(max_length=100)
    instrument_type = models.ForeignKey(InstrumentType, on_delete=models.CASCADE, blank=True, null=True)
    specialties = models.ManyToManyField(Specialty, related_name='instruments')
    image = models.ImageField(upload_to='instrument_images/', blank=True, null=True)
    model_embed_code1 = models.TextField(blank=True, null=True)
    model_embed_code2 = models.TextField(blank=True, null=True)
    model_embed_code3 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_embed_codes(self):
        return [code for code in [self.model_embed_code1, self.model_embed_code2, self.model_embed_code3] if code]
    
    def get_random_question(self):
        return random.choice(self.questions.all())
    
class QuizQuestion(models.Model):
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()

    def __str__(self):
        return f"Q: {self.question_text} - {self.instrument.name}"
    
class Instrument_NameAndDescription(models.Model):
    instrumentType = models.ForeignKey(InstrumentType, on_delete=models.CASCADE)
    specificInstrument = models.CharField(max_length=100)
    description = models.TextField(blank=False)

    def __str__(self):
        return str(self.instrumentType)
    
class QuizChoice(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
