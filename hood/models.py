from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from tinymce.models import HTMLField

# Create your models here.
class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=30)

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls,neighborhood_id):
        neighborhood = cls.objects.get(id=neighborhood_id)
        return neighborhood
