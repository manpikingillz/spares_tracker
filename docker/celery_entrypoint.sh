echo "--> Starting celery process"
celery -A spares_tracker.tasks beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler