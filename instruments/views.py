from django.shortcuts import render

# Create your views here.

def instrument_hub_view(request):
    return render(request, "pages/instruments/instrument-hub.html")
