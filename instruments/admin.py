from django.contrib import admin
from .models import Specialty, Instrument, QuizQuestion

# Register your models here.

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_specialties']
    
    def get_specialties(self, obj):
        return ", ".join([s.name for s in obj.specialties.all()])
    get_specialties.short_description = 'Specialties'

@admin.register(QuizQuestion)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'instrument']
    search_fields = ['question_text']
    list_filter = ['instrument']