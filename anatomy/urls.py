from django.urls import path
from . import views

urlpatterns = [
    path("", views.anatomy_main_view, name='anatomy_main'),
]