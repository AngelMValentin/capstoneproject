from django.shortcuts import render
from django.views.generic import ListView

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
