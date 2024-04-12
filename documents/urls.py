# documents/urls.py

from django.urls import path
from .views import document_upload, document_list

urlpatterns = [
    path('upload/', document_upload, name='document_upload'),
    path('', document_list, name='document_list'),
]
