from django.shortcuts import render

# Create your views here.
# entries/views.py
from .models import Entry


def index(request):
    """Show all entries."""
    entries = Entry.objects.all()
    return render(request, 'entries/index.html', {'entries': entries})
