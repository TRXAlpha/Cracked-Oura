# Use a lightweight Python base image
FROM python:3.11-slim

# Set the working directory to the parent so 'backend' exists
WORKDIR /app

# Copy the requirements file
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright
RUN playwright install chromium
RUN playwright install-deps chromium

# COPY the backend folder into /app/backend
# This creates /app/backend/src/... which matches your import path!
COPY backend/ /app/backend/

# Set the Python path so it can find the 'backend' folder
ENV PYTHONPATH="/app"

# Start the FastAPI server (pointing to the nested path)
CMD ["uvicorn", "backend.src.api.main:app", "--host", "0.0.0.0", "--port", "10000"]
