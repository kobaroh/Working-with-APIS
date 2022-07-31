from django.contrib.auth.models import user
from django.db import models
from django.utils import timezone
# Create your models here.

class Link(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published')
    )
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20)
    author = models.ForeignKey(get_user_model, on_delete=models.CASCADE, related_name='links_posts')
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


class Meta:
    ordering = ('-publish')


def __str__(self):
    return self.title