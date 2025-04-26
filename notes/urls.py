from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.list, name='notes_list'),
    path("create/", views.NoteCreate.as_view(), name="note_create"),
    path("details/<int:pk>/", views.NoteDetail.as_view(), name='note_detail'),
    path("update/<int:pk>/", views.NoteUpdate.as_view(), name='note_update'),
    path("delete/<int:pk>/", views.NoteDelete.as_view(), name='note_delete'),
]