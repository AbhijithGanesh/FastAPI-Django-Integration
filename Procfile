python-3.9.5
web: gunicorn TestingProject.asgi:app  -w 4 -k uvicorn.workers.UvicornWorker 
python manage.py makemigrations
python manage.py migrate
