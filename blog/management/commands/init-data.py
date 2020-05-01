from django.core.management import BaseCommand

from blog.models import Blog


class Command(BaseCommand):
    help = 'initiate data for the blog'

    def handle(self, *args, **options):
        Blog.objects.get_or_create(title='first title for the blog',
                                   text='first text for the blog, first text for the blog',
                                   image='/init-images/test11.jpg',
                                   published_at='2012-05-01 00:00:00')
        Blog.objects.get_or_create(title='second title for the blog',
                                   text='second text for the blog, second text for the blog',
                                   image='/init-images/test12.jpg',
                                   published_at='2012-04-01 00:00:00')
        Blog.objects.get_or_create(title='third title for the blog',
                                   text='third text for the blog, third text for the blog',
                                   image='/init-images/test13.jpg',
                                   published_at='2012-03-01 00:00:00')

        self.stdout.write(self.style.SUCCESS('Successfully initiated data'))
