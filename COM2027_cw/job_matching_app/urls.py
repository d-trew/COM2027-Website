# job_matching_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_opportunities, name='job_opportunities'),
    # Add other URLs as needed
]
