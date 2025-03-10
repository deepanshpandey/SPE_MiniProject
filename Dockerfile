FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY calculator.py caltest.py /app/

# Default command to run the application
CMD ["python3", "/app/calculator.py"]
