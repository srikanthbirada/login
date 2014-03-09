from django.db import models

# Create your models here.
class Owner(models.Model):
	owner_id = models.PositiveIntegerField(max_length=20)
	name = models.CharField(max_length=20)
	mobile_number=models.PositiveIntegerField(max_length=10)
	email=models.EmailField()

class VenueList(models.Model):
	owner_id = models.ManyToManyField(Owner)
	venue_id = models.PositiveIntegerField(max_length=20)
	name = models.CharField(max_length=20)
	address = models.CharField(max_length=50)
