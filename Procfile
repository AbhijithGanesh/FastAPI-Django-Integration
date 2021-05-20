python-3.9.5
web: gunicorn TestingProject.asgi:app  -w 4 -k uvicorn.workers.UvicornWorker 
web: bin/start-nginx unicorn -c config/unicorn.rb -c gunicorn.conf.py TestingProject.asgi
python manage.py makemigrations
python manage.py migrate
