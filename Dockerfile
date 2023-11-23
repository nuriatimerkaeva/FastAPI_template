FROM python:3.10.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y postgresql postgresql-contrib gcc python3-dev musl-dev
RUN pip install --upgrade pip
WORKDIR /src

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
EXPOSE 8000
COPY . .