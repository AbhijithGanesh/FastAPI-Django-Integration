python-3.9.5
web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker TestingProject.asgi:app 
python manage.py makemigrations
python manage.py migrate
