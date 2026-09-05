import os
from celery import Celery

# tellnig celery where to finds djngo settings 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# celery application instance
# for anyone wondering why I named it config the same name as my config file its just by convention
app = Celery('config')

# loaidng celery related settings from Django settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# auto discover a tasks.py file inside all installed django app

app.autodiscover_tasks()