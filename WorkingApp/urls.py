
from django.urls import path
from WorkingApp.views import LandingPage


urlpatterns = [
    path('', LandingPage)
]


