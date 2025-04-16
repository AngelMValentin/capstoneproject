from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="root"),
    path("home/", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path('flashcards/', views.flashcard_home, name='flashcard_home'),
    path('flashcards/<slug:slug>/<int:card_index>/', views.flashcard_set, name='flashcard-set'),
]