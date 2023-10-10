# Author: Jakhongir Ruzibaev
# Created At: 11/10/2023

# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app to use cache
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# make migrations
RUN python manage.py makemigrations

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run your app when the container starts
CMD ["python", "manage.py", "runserver", "8000"]