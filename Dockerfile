FROM python:3.11-slim

# Set working directory
# WORKDIR /app

# Copy application files
COPY calculator.py caltest.py

# Default command to run the application
CMD ["python3", "calculator.py"]
