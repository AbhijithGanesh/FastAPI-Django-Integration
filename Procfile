python-3.9.5
web: gunicorn TestingProject.asgi:app  -w 4 -k uvicorn.workers.UvicornWorker 
web: bin/start-nginx bundle exec unicorn -c config/unicorn.rb
python manage.py makemigrations
python manage.py migrate
