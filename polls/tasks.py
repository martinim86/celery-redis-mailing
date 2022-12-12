# from .celeryapp import shared_task
from hello_django.celery import app
from datetime import timedelta
from polls.service import send

@app.task()
def test():
    send()
    return True



app.conf.timezone = 'UTC'