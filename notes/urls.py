from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.list, name='notes_list'),
    path("create/", views.NoteCreate.as_view(), name="note_create"),
]