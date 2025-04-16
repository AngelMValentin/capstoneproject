from django.contrib import admin

# Register your models here.

from .models import Flashcard

@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('question', 'topic', 'chapter')
    search_fields = ('question', 'answer', 'topic', 'chapter')
    list_filter = ('chapter', 'topic')