# job_matching_app/models.py

from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class JobOpportunity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # Add other fields as needed

    def __str__(self):
        return self.title
