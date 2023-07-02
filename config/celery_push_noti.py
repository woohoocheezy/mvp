from __future__ import absolute_import
from django.conf import settings
import os
from celery import Celery
from celery.schedules import crontab

# from fcm_test import send_push_notifications

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "send_push_notifications": {
        "task": "push_notification.tasks.send_push_notifications",
        # "schedule": crontab(minute=0, hour=14),  # Execute every day at 2 PM
        "schedule": crontab(minute=0, hour=11),  # Execute every day at 2 PM
    }
}
