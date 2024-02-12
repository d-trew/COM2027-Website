import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection

class Command(BaseCommand):
    help = 'Reset the database, apply migrations, and seed data'

    def handle(self, *args, **options):
        # Remove the existing SQLite database file
        db_file_path = 'db.sqlite3'
        if os.path.exists(db_file_path):
            os.remove(db_file_path)
            self.stdout.write(self.style.SUCCESS('Removed the existing SQLite database file.'))

        # Create a new SQLite database file
        self.stdout.write(self.style.SUCCESS('Creating a new SQLite database file...'))
        open(db_file_path, 'w').close()

        # Make migrations
        self.stdout.write(self.style.SUCCESS('Creating new migrations...'))
        call_command('makemigrations')

        # Apply migrations
        self.stdout.write(self.style.SUCCESS('Applying migrations...'))
        call_command('migrate')
        
        # Seed the database
        self.stdout.write(self.style.SUCCESS('Seeding the database...'))
        call_command('seed')

        self.stdout.write(self.style.SUCCESS('Database reset successfully.'))
