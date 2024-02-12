# job_matching_app/management/commands/seed.py

import random
from faker import Faker
from job_matching_app.models import Student, JobOpportunity
from django.core.management.base import BaseCommand

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write("Seeding data...")

        num_students = 10
        num_jobs = 20

        self.create_students(num_students)
        self.create_job_opportunities(num_jobs)

        self.stdout.write(self.style.SUCCESS("Seed data has been successfully generated."))

    def create_students(self, num_students):
        students = []
        for _ in range(num_students):
            student = Student(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                skills="Python, Django, HTML, CSS",  # Example skills
                # Add other fields as needed
            )
            students.append(student)
        Student.objects.bulk_create(students)

    def create_job_opportunities(self, num_jobs):
        job_opportunities = []
        for _ in range(num_jobs):
            job_opportunity = JobOpportunity(
                title=fake.job(),
                description=fake.text(),
                skills_required="JavaScript, React",  # Example skills_required
                # Add other fields as needed
            )
            job_opportunities.append(job_opportunity)
        JobOpportunity.objects.bulk_create(job_opportunities)
