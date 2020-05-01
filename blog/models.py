from django.utils import timezone
from tinymce.models import HTMLField
from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=100, blank=False)
    published_at = models.DateTimeField(default=timezone.now)
    text = HTMLField()
    image = models.ImageField()

    def __str__(self):
        return self.title
