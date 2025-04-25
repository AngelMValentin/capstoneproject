from django.urls import path
from . import views

urlpatterns = [
    path('instruments/', views.instrument_hub_view, name='instrument_hub'),
    path('<slug:slug>/<int:index>/', views.instrument_main_view, name='instrument_main'),
]