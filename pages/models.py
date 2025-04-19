from django.db import models


# Create your models here.

class Flashcard(models.Model):
    chapter = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"{self.topic} - {self.question[:50]}"
