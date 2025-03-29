# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . /app

# Expose the port the app runs on
EXPOSE 8000

# Set the environment variable for FastAPI (optional)
ENV PYTHONUNBUFFERED=1

# Run the FastAPI application using Uvicorn

CMD ["uvicorn", "FastAPI:app", "--host", "0.0.0.0", "--port", "8000"]


