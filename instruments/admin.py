from django.contrib import admin
from .models import Specialty, Instrument, QuizQuestion, InstrumentType, Instrument_NameAndDescription, QuizChoice

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

@admin.register(InstrumentType)
class InstrumentTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

@admin.register(Instrument_NameAndDescription)
class NameAndDescriptionAdmin(admin.ModelAdmin):
    list_display = ['instrumentType', 'specificInstrument', 'description']

@admin.register(QuizChoice)
class QuizChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'choice_text', 'is_correct']