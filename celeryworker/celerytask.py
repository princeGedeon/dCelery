import os

from celery import Celery


app = Celery('task')

app.config_from_object('celeryconfig')
app.conf.imports=('app.tasks')
app.autodiscover_tasks()
