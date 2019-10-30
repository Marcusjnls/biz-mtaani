from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from tinymce.models import HTMLField

# Create your models here.
class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=30)
