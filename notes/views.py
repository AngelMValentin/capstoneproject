from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Note
from django.urls import reverse_lazy
from .forms import NoteForm

# Create your views here.

"""
Class-based views:

View        = generic view
ListView    = get a list of records
DetailView  = get a single(detail) record
CreateView  = create a new record
DeleteView  = remove a record
UpdateView  = modify an existing record
LoginView   = login
"""


def list(request):
    return render(request, 'notes/list.html')

class NoteList(ListView):
    model = Note
    template_name = 'notes/list.html'
    context_object_name = 'all_notes'

class NoteCreate(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/create.html'
    success_url = reverse_lazy('notes_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Create New Note"
        return context

class NoteDetail(DetailView):
    template_name = 'notes/details.html'
    model = Note

class NoteUpdate(UpdateView):
    template_name = 'notes/update.html'
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy("notes_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_title"] = "Update Note"
        return context
    

class NoteDelete(DeleteView):
    model = Note
    template_name = 'note/delete.html'
    success_url = reverse_lazy('notes_list')

    
