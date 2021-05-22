python-3.9.5
python manage.py collectstatic
web: gunicorn TestingProject.asgi:app -w 4 -k uvicorn.workers.UvicornWorker  
python manage.py makemigrations
python manage.py migrate
