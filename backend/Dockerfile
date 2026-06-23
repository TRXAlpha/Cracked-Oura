# Use a lightweight Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install Python packages
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright, Chromium, and all OS-level dependencies (running as root)
RUN playwright install chromium
RUN playwright install-deps chromium

# Copy the rest of your backend files into the container
COPY backend/ .

# Set the Python path so it can find your src folder
ENV PYTHONPATH="/app"

# Start the FastAPI server
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "10000"]
