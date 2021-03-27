FROM python:3.9.2

WORKDIR /src

COPY . /src

RUN apt-get update && apt-get install postgresql-client -y gettext
RUN pip install -r /src/requirements.txt