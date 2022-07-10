echo "--> Starting beats process"
celery -A spares_tracker.tasks worker -l info --without-gossip --without-mingle --without-heartbeat