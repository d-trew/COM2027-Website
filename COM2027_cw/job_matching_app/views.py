# job_matching_app/views.py

from django.shortcuts import render
from .models import JobOpportunity

def job_opportunities(request):
    job_opportunities = JobOpportunity.objects.all()
    context = {'job_opportunities': job_opportunities}
    return render(request, 'job_matching_app/job_opportunities.html', context)
