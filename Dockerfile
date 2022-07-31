# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# configure the container to run in an executed manner
EXPOSE 5000

CMD ["python", "main.py"]