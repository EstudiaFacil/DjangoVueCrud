# syntax=docker/dockerfile:1

FROM python:3.11.4-slim-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/backend

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver"]
