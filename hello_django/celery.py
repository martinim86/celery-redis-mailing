from __future__ import absolute_import
import os, sys
from datetime import timedelta
from celery.schedules import crontab
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hello_django.settings')

app = Celery('hello_django')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# app.conf.beat_shedule = {
#     'send_spam':{
#         'task' : 'polls.tasks.test',
#         'schedule': timedelta(seconds=3)
#     }
# }