
from django.urls import path
from WorkingApp.views import LandingPage

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', LandingPage)
]

urlpatterns.append(staticfiles_urlpatterns())
