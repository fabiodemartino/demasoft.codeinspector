FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all contents of celery-worker directory
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Make sure the start script is executable
RUN chmod +x ./celery_start.sh

# Set the entrypoint (optional if using docker-compose command)
CMD ["./celery_start.sh"]
