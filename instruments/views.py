from django.shortcuts import render, get_object_or_404
from .models import Instrument, Specialty, InstrumentType

# Create your views here.

def instrument_hub_view(request):
    InstrumentTypes = InstrumentType.objects.all()
    return render(request, "pages/instruments/instrument-hub.html", {'InstrumentTypes': InstrumentTypes})

def instrument_main_view(request, slug):
    specialty = get_object_or_404(InstrumentType, slug=slug)
    instruments = Instrument.objects.filter(instrument_type__slug=slug)
    return render(request, 'pages/instruments/instrument-main.html', {
        'specialty': specialty,
        'instruments': instruments,
        })
    
