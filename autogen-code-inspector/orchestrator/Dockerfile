# Use a Python base image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy the orchestrator app's source code into the container
COPY . .

# Install any Python dependencies (add requirements.txt if necessary)
RUN pip install --no-cache-dir -r requirements.txt

# Expose necessary port (for example, 5000 if it runs a Flask app)
EXPOSE 6000

# Command to run the orchestrator app
CMD ["python", "main.py"]
