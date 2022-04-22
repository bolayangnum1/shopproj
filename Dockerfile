
FROM python:3.9
WORKDIR /app/
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python manage.py makemigrations data
RUN python manage.py migrate
COPY . /app