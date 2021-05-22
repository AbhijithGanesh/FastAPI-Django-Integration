from django.contrib import admin
from django.urls import path, include, re_path
from .views import On_Landing

urlpatterns = [
    path('admin', admin.site.urls),
    path('', On_Landing),
    path('Project/', include('WorkingApp.urls')),
]


