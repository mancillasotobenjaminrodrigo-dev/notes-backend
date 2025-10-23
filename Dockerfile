FROM python:3.10-slim

RUN apt-get update && apt-get install -y gcc && apt-get clean

WORKDIR /app

COPY . .

ENV GOOGLE_APPLICATION_CREDENTIALS=/app/sensitive/service-account.json

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--workers", "1","--timeout-keep-alive", "0", "--host", "0.0.0.0", "--port", "8080"] 
