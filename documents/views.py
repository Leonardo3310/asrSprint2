from django.shortcuts import render

# Create your views here.
# documents/views.py

from .models import Document
from .forms import DocumentForm

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
