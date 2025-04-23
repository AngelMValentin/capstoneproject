from django.db import models
import random

# Create your models here.

class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Instrument(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    specialties = models.ManyToManyField(Specialty, related_name='instruments')
    image = models.ImageField(upload_to='instrument_images/', blank=True, null=True)
    model_embed_code = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_random_question(self):
        return random.choice(self.questions.all())
    
class QuizQuestion(models.Model):
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    correct_choice = models.CharField(max_length=255)

    def __str__(self):
        return f"Q: {self.text} - {self.instrument.name}"
