from django.shortcuts import render, get_object_or_404
from .models import AnatomyMain, AnatomySystem
from instruments.models import Specialty

# Create your views here.

def anatomy_main_view(request):
    specialties = Specialty.objects.all()
    anatomy = AnatomyMain.objects.all()
    systems_by_specialty = {}

    for specialty in specialties:
        systems = AnatomySystem.objects.filter(specialty=specialty)
        systems_by_specialty[specialty.id] = systems

    return render(request, "anatomy/anatomy_main.html", {
        'specialties': specialties,
        'anatomy': anatomy,
        'systems_by_specialty': systems_by_specialty,
    })

def systems_view(request, slug):
    main_entry = get_object_or_404(AnatomyMain, slug=slug)
    systems = AnatomySystem.objects.filter(specialty=main_entry.system.specialty).order_by('id')
    current_index = list(systems).index(main_entry.system)
    next_index = (current_index + 1) % systems.count()
    next_system = systems[next_index]

    return render(request, "anatomy/systems.html", {
        'system': main_entry.system,
        'next_slug': AnatomyMain.objects.get(system=next_system).slug
    })
