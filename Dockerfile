FROM python:3-alpine

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["python3", "app.py"]