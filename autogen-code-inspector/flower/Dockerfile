FROM python:3.9

WORKDIR /app

# Install Flower
RUN pip install flower

# Default command to run Flower
CMD ["flower", "--port=5555", "--broker=redis://redis:6379/0"]
