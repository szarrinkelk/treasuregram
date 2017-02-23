from django.shortcuts import render
#from django.http import HttpResponse
from .models import Treasure

#creating our views here
def index(request):
	#here we need to get all of the Treasure's objects
	print Treasure
	print dir(Treasure)
	treasures = Treasure.objects.all()

	"""
	name = 'Gold Nugget'
	value = 1000.00
	#A context is a dict that maps template variable names to Python objects
	
	context = {'treasure_name': name,
				'treasure_val' : value
	}
	"""

	#return HttpResponse('<h1>Hello Explorers!</h1>')
	return render(request, 'index.html', {'treasures':treasures}) 
	#We can pass the context as a 3rd parameter to our render() function
	#we put the context in directly instead of creating a context variable first


#Treasure class to store attributes

#class Treasure:
#	def __init__(self, name, value, material, location, img_url):
#		self.name = name
#		self.value = value
#		self.material = material
#		self.location = location
#		self.img_url = img_url

#list of all of our treasures(to create our context)
#treasures = [
#	Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM", 'http://cdn.gemrockauctions.com/uploads/images/75000-79999/77914/77914_1234494758.jpg' ),
# 	Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO", 'http://www.sciencebuzz.org/sites/default/files/images/2004-04.jpg'),
# 	Treasure('Coffee Can', 20.00, 'tin', 'Acme, CA', 'http://chemicool.com/elements/images/300-tin-ore.jpg')
# ] 