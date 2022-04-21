
FROM python:3.9
WORKDIR /app/
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get -y install python-pip
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install psycopg2-binary
COPY . /app