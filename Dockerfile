FROM python:3.8.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /App
WORKDIR /App
ADD . /App/
RUN pip install -r requirements.txt