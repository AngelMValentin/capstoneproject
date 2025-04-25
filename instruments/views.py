from django.shortcuts import render, get_object_or_404
from .models import Instrument, Specialty

# Create your views here.

def instrument_hub_view(request):
    specialties = Specialty.objects.all()
    return render(request, "pages/instruments/instrument-hub.html", {'specialties': specialties})

def instrument_main_view(request, slug, index):
    index = int(request.GET.get('index', 0))
    specialty = get_object_or_404(Specialty, slug=slug)
    instruments = Instrument.objects.filter(specialties=specialty)
    return render(request, 'pages/instruments/instrument-main.html', {
        'specialty': specialty,
        'instruments': instruments,
        'index': index
        })
    
