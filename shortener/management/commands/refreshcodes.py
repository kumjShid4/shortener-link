from django.core.management.base import BaseCommand, CommandError
from shortener.models import URL

class Command(BaseCommand):
    help = "Refresh all the short codes."
    # def add_arguments(self, parser):
    #     parser.add_arguments()

    def handle(self, *args, **options):
        return URL.objects.refresh_codes()
