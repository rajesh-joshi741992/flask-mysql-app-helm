# Use a lightweight base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the application’s port 8080
EXPOSE 8080

# Set environment variables for database connection
ENV MYSQL_SERVER=127.0.0.1
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=your_password
ENV MYSQL_DB=test_db

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080

# Command to run the Flask app
CMD ["flask", "run"]
