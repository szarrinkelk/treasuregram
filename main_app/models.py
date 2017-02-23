from django.db import models #imports the model class

# Create a class that inherits from models.model so that django knows we're creating a model

class Treasure(models.Model):
	#a model describes how we want to store the data in a database 
	name = models.CharField(max_length=100) #use special model types that correspond to database types
	value = models.DecimalField(max_digits=10, decimal_places=2)
	material = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	img_url = models.CharField(max_length=255)

	def __str__(self):
		return self.name
