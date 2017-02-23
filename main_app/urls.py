from django.conf.urls import url
from . import views 
"""
if you want to import a specific module from your current app, you can leave off
the package and type the following: from . import module
"""

urlpatterns = [
	#this pattern checks that the URL has an empty path, which will go to the homepage
	#the $ terminates the regex
	url(r'^$', views.index),

]