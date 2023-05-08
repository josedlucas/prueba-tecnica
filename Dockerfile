FROM ubuntu/apache2:latest

RUN rm -rf /var/www/html/*
COPY ./frontApp/src /var/www/html
EXPOSE 80
