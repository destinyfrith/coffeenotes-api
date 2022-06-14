"""Coffee Notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from coffeenotesapi.views import register_user, login_user
from django.conf.urls import include
from rest_framework import routers

from coffeenotesapi.views.brewingmethod import BrewingMethodView
from coffeenotesapi.views.entry import EntryView
from coffeenotesapi.views.flavornote import FlavorNoteView

# The trailing_slash=False tells the router to accept /brewingmethods instead of /brewingmethods/
router = routers.DefaultRouter(trailing_slash=False)
# The next line is what sets up the /brewingmethods resource.
# The first parameter, r'brewingmethods, is setting up the url. The second BrewingMethodView is telling the server which view to use when it sees that url.
# The third, brewingmethod, is called the base name. You’ll only see the base name if you get an error in the server.
# It acts as a nickname for the resource and is usually the singular version of the url.
router.register(r'brewingmethods', BrewingMethodView, 'gametype')
router.register(r'flavornotes', FlavorNoteView, 'flavornote')
router.register(r'entries',EntryView, 'entry')

urlpatterns = [
    # Requests to http://localhost:8000/register will be routed to the register_user function
    path('register', register_user),
    # Requests to http://localhost:8000/login will be routed to the login_user function
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]