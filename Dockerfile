# Use a lightweight Python image.
FROM python:3.9-slim

# Set the working directory.
WORKDIR /app

# Copy the application file.
COPY app.py /app

# Install Flask and requests.
RUN pip install Flask requests

# Expose the port (Render will supply this as an env variable).
EXPOSE 8080

# Define the command to run the application.
CMD ["python", "app.py"]
