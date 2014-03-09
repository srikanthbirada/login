from django.db import models

# Create your models here.
class VenueList(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=15)
	OwnerName = models.CharField(max_length=20)
	Contact = models.
