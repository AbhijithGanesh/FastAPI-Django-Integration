import os
#Importing Django Requirements
from django.apps import apps #Used to access Installed Apps, will result in an ImproperlyCOnfigured Error if not followed right
from django.conf import settings #Used to accesss the parameters of settings
from django.core.wsgi import get_wsgi_application #ASGI gateway option was not available when this project was integrated with Django

#Importing FastAPI features
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.wsgi import WSGIMiddleware
from starlette.middleware.cors import CORSMiddleware


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TestingProject.settings")
apps.populate(settings.INSTALLED_APPS)

#Do not Import the Views before configuring the apps, If done so, it will result in an ImproperlyConfigured Exception


#Importing the Views from API Module to route the API
from api.views import router,router2


def get_application():
    app = FastAPI(title=settings.PROJECT_NAME, debug=settings.DEBUG)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(router, prefix="/api")
    app.include_router(router2,prefix='/v2') #Example Where Multiple Routers can be mapped.
    
    app.mount("/Application", WSGIMiddleware(get_wsgi_application()))
    #FastAPI doesn't have a ASGIMiddleWare --> Version:0.65.1

    app.mount("/static", StaticFiles(directory="static"), name="static")

    #This will include all the static files in the statics folder
    return app


app = get_application()