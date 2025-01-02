# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy the service code
COPY patient_record_service.py /app/patient_record_service.py

# Expose the port the app runs on
EXPOSE 8000

# Define environment variable
ENV FLASK_APP=patient_record_service.py

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
