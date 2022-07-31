from django.contrib.auth import get_user_model
from django.db import models


class post(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=200, blank=True, unique=True)
    author = get_user_model()
    created_date = models.DateTimeField()
    active = models.BooleanField(default=True)
