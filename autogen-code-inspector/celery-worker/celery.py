from celery import Celery

# Create a Celery application instance
app = Celery('tasks', broker='redis://redis:6379/0')

# Optionally, load task modules from all registered Django app configs.
app.config_from_object('celeryconfig')

# Automatically discover tasks in all registered Django app configs.
app.autodiscover_tasks()

@app.task
def add(x, y):
    return x + y
