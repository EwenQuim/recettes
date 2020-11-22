FROM python:3.9
LABEL maintainer='ewenquim'
EXPOSE 8000

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /backend

# We changing modules is less frequent than changing code
RUN pip install --upgrade pip
COPY requirements.txt /backend
RUN pip install -r requirements.txt
