# Use a base image with Python
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your project files (including model and app.py) into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app will run on
EXPOSE 5000

# Command to run your application
CMD ["python", "app.py"]
