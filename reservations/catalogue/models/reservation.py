# catalogue/models/reservation.py
from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Reservation {self.id} - {self.status}"
