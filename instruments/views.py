from django.shortcuts import render, get_object_or_404
from .models import Instrument, Specialty, InstrumentType, Instrument_NameAndDescription, QuizChoice, QuizQuestion
import random

# Create your views here.

def instrument_hub_view(request):
    InstrumentTypes = InstrumentType.objects.all()
    return render(request, "pages/instruments/instrument-hub.html", {'InstrumentTypes': InstrumentTypes})

def instrument_main_view(request, slug):
    InstrumentTypes = get_object_or_404(InstrumentType, slug=slug)
    instruments = Instrument.objects.filter(instrument_type__slug=slug)
    name_and_descriptions = Instrument_NameAndDescription.objects.filter(instrumentType=InstrumentTypes)

    questions = QuizQuestion.objects.filter(instrument__in=instruments)
    question = random.choice(questions) if questions.exists() else None
    choices = list(question.choices.all()) if question else []
    random.shuffle(choices)

    return render(request, 'pages/instruments/instrument-main.html', {
        'InstrumentTypes': InstrumentTypes,
        'instruments': instruments,
        'name_and_descriptions': name_and_descriptions,
        'question': question,
        'choices': choices,
        })
    
