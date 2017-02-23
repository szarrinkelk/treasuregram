from django.conf.urls import include, url
from django.contrib import admin
from main_app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Treasuregram.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #localhost:8000 will go here
    url(r'^', 
    	include('main_app.urls')),
]
