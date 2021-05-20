from django.contrib import admin
from django.urls import path, include
from .views import On_Landing
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns(
    path('admin/', admin.site.urls),
    path('', On_Landing),
    path('Project/', include('WorkingApp.urls'))
)

urlpatterns+staticfiles_urlpatterns()
