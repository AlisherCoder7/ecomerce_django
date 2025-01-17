# Use the official Python image from the Docker Hub
FROM python:3.12.5

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory to your project folder
WORKDIR /django_rest_framework

# Copy requirements.txt into the container and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /django_rest_framework/

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
