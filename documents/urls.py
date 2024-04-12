# documents/urls.py

from django.urls import path
from .views import document_upload, document_list, get_logs, generate_synthetic_logs, get_synthetic_logs

urlpatterns = [
    path('upload/', document_upload, name='document_upload'),
    path('', document_list, name='document_list'),
    path('logs/', get_logs, name='get_logs'),
    path('generate-logs/', generate_synthetic_logs, name='generate_logs'),
    path('synthetic-logs/', get_synthetic_logs, name='get_synthetic_logs'),
]
