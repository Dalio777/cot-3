FROM python:3.9-slim

WORKDIR /app

COPY img_create.py /app/img_create.py

RUN pip install pillow minio

CMD ["python3", "img_create.py"]