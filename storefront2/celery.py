import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "storefront2.settings")

celery = Celery("storefront2")
celery.config_from_object("django.conf:settings", namespace="CELERY")
celery.autodiscover_tasks()