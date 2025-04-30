from django.contrib import admin
from .models import Note, NoteComment

admin.site.register(Note)
admin.site.register(NoteComment)

# Register your models here.
