# CampusBuddy API container
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY campus_tools.py agent.py app.py ./

# Run as a normal user, not root
RUN useradd --create-home appuser
USER appuser

# Cloud Run and most hosts tell the app which port to use through $PORT
ENV PORT=8080
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT}"]
