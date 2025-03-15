FROM python:3.9

RUN pip install prometheus_client psutil

COPY exporter.py .

WORKDIR /app

CMD ["python", "exporter.py"]