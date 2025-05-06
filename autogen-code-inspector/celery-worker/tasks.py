from celery import Celery

# Import your Celery app instance
from celery_worker.celery import app  # Assuming your celery.py file is in 'celery_worker'

# Define tasks
@app.task
def add(x, y):
    """A simple task that adds two numbers"""
    return x + y

@app.task
def multiply(x, y):
    """A task that multiplies two numbers"""
    return x * y

@app.task
def fetch_data_from_db():
    """Simulate a database fetch task"""
    # Simulating a long-running operation
    # Replace with actual database logic
    return "Fetched data from the database"
