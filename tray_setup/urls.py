from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_tray_view, name='main_tray_view'),
]