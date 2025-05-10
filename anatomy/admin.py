from django.contrib import admin
from .models import AnatomyMain, AnatomySystem

# Register your models here.

@admin.register(AnatomyMain)
class AnatomyMainAdmin(admin.ModelAdmin):
    list_display = ['specialty', 'system', 'slug']

@admin.register(AnatomySystem)
class AnatomySystemAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialty']
