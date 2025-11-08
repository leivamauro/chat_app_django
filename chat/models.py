from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RoomsModel(models.Model):

    name = models.CharField(max_length=20)
    user = models.ManyToManyField(User, related_name="rooms_joined", blank=True)

    def __str__(self):
        return f"Sala: {self.name}"
