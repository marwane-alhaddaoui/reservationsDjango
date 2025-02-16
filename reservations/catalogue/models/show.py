from django.db import models
from .location import *

# Create your models here.
class Show(models.Model):
   slug = models.CharField(max_length=60, unique=True)
   title = models.CharField(max_length=255)
   description = models.TextField(max_length=255, null=True)  # Permet NULL
   poster_url = models.CharField(max_length=255, null=True)  # Permet NULL
   duration = models.PositiveSmallIntegerField(null=True)  # Permet NULL
   created_in = models.PositiveSmallIntegerField(null=True)  # Permet NULL
   location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='shows')
   bookable = models.BooleanField(default=True, null=True)  # Permet NULL
   created_at = models.DateTimeField(auto_now_add=True, null=True)  # Permet NULL
   updated_at = models.DateTimeField(auto_now=True, null=True)  # Permet NULL
    
def __str__(self):
        return self.title
    
class Meta:
        db_table = "shows"
