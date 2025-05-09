from django.shortcuts import render
from .models import AnatomyMain
from instruments.models import Specialty

# Create your views here.

def anatomy_main_view(request):
    specialties = Specialty.objects.all()
    anatomy = AnatomyMain.objects.all()
    return render(request, "anatomy/anatomy_main.html", {
        'specialties': specialties,
        'anatomy': anatomy,
    })


