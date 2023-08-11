from django.core.management.base import BaseCommand
from myapp.models import Post

class Command(BaseCommand):
    help = 'Delete all posts'

    def handle(self, *args, **options):
        Post.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All posts have been deleted.'))
