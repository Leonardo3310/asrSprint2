from django.shortcuts import render

# Create your views here.
# documents/views.py

from .models import Document
from .forms import DocumentForm
from django.http import HttpResponse
import json  

def document_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'documents/upload_complete.html', {'form': form})
    else:
        form = DocumentForm()
    return render(request, 'documents/document_upload.html', {'form': form})

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'documents/document_list.html', {'documents': documents})

# documents/views.py

def get_logs(request):
    logs = [
        {"id": 1, "content": "Log entry 1", "timestamp": "2024-04-09 12:00:00"},
        {"id": 2, "content": "Log entry 2", "timestamp": "2024-04-09 12:05:00"},
        {"id": 3, "content": "Log entry 3", "timestamp": "2024-04-09 12:10:00"}
    ]
    return render(request, 'documents/logs.html', {'logs': logs})
