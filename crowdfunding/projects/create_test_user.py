from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command00(BaseCommand):
    help = 'Create a test user for development or testing'

    def handle(self, *args, **options):
        User = get_user_model()
        username = 'testuser2'
        password = 'bigbadothertester'

        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password)
            self.stdout.write(self.style.SUCCESS(f'Test user {username} created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Test user {username} already exists'))

class Command01(BaseCommand):
    help = 'Create a test user for development or testing'

    def handle(self, *args, **options):
        User = get_user_model()
        username = 'testuser01'
        password = 'TrickleUpholdDelegatorSucculent'

        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password)
            self.stdout.write(self.style.SUCCESS(f'Test user {username} created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Test user {username} already exists'))

class Command03(BaseCommand):
    help = 'Create a test user for development or testing'

    def handle(self, *args, **options):
        User = get_user_model()
        username = 'testcister01'
        password = 'ExcusableDawnUntoastedSupplier'

        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password)
            self.stdout.write(self.style.SUCCESS(f'Test user {username} created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Test user {username} already exists'))