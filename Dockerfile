FROM python:3.12.4-alpine3.20

ENV PYTHONIOENCODING UTF-8
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_PASSWORD=1qaz@WSX89

WORKDIR /usr/src/app

COPY req.txt ./
RUN pip install --no-cache-dir -r req.txt

RUN mkdir static && mkdir media
COPY . .
CMD python manage.py makemigrations && python manage.py migrate &&  python manage.py createsuperuser --email admin@admin.com --noinput && python manage.py runserver 0.0.0.0:8000
EXPOSE 8000