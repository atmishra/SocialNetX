web: gunicorn config.wsgi:application
worker: celery worker --app=SocialNetX.taskapp --loglevel=info
