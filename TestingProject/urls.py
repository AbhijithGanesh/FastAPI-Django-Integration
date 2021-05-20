from django.contrib import admin
from django.urls import path, include
from .views import On_Landing
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, patterns
urlpatterns = patterns(
    url('admin/', admin.site.urls),
    url('', On_Landing),
    url('Project/', include('WorkingApp.urls'))
)

urlpatterns+staticfiles_urlpatterns()
