from django.shortcuts import render
from .models import Flashcard

def home_view(request):
    return render(request, "pages/home.html")

def about_view(request):
    return render(request, "pages/about.html")
# Create your views here.

def flashcard_home(request):
    chapters = [
        {
            "title": "Core Concepts",
            "slug": "core-concepts",
            "topics": [
                "Orientation to Surgical Technology",
                "Legal Concepts, Risk Management, and Ethical Issues",
                "The Surgical Patient",
                "Special Populations",
                "Physical Environment and Safety Standards"
            ]
        },
        {
            "title": "Principles and Practice",
            "slug": "principles-and-practice",
            "topics": [
                "Biomedical Science and Minimally Invasive Surgery",
                "Preventing Perioperative Disease Transmission",
                "Emergency Situations and All-Hazards Preparation",
                "Surgical Pharmacology and Anesthesia",
                "Instrumentation, Equipment, and Supplies",
                "Hemostasis, Wound Healing, and Wound Closure",
                "Surgical Case Management"
            ]
        },
        {
            "title": "Surgical Procedures",
            "slug": "surgical-procedures",
            "topics": [
                "Diagnostic Procedures",
                "General",
                "Obstetric and Gynecologic",
                "Ophthalmic",
                "Otohinolaryngologic",
                "Oral and Maxillofacial",
                "Plastic and Reconstructive",
                "Genitourinary",
                "Orthopedic",
                "Cardiothoracic",
                "Peripheral Vascular",
                "Neuro"
            ]
        }
    ]
    return render(request, 'pages/FC-Categories.html', {'chapters': chapters})

CHAPTER_SLUG_MAP = {
    "core-concepts": "Core Concepts",
    "principles-and-practice": "Principles and Practice",
    "surgical-procedures": "Surgical Procedures",
}

def flashcard_set(request, slug, card_index):
    chapter_title = CHAPTER_SLUG_MAP.get(slug)
    if not chapter_title:
        return render(request)
    
    flashcards = Flashcard.objects.filter(chapter=chapter_title)

    if not flashcards.exists():
        return render(request, 'pages/flashcard_set.html', {
            'title': chapter_title,
            'flashcard': None,
            'card_index': 0,
            'flashcards': []
        })

    
    card_index = int(card_index)
    if card_index >= len(flashcards):
        card_index = len(flashcards) - 1

    flashcard = flashcards[card_index]
    

    flashcards = Flashcard.objects.filter(chapter=chapter_title)
    return render(request, 'pages/flashcard_set.html', {
        'flashcard': flashcard,
        'flashcards': flashcards,
        'title': chapter_title,
        'card_index': card_index,
        'slug': slug
    })


