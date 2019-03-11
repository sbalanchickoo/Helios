FROM ubuntu:18.04
ENV DEBIAN_FRONTEND noninteractive

LABEL maintainer "Srikant Balan <summer.street.guy@gmail.com>"
LABEL description "Nginx + uWSGI + Flask based on Ubuntu Linux and managed by Supervisord"

# Copy python requirements file
COPY requirements.txt /tmp/requirements.txt

RUN apt-get update
#RUN apt-get install dialog apt-utils -y 
RUN apt-get install -y \
    python3 \
    python3-pip \
    nginx \
    uwsgi \
    uwsgi-plugin-python3 \
    supervisor && \
    pip3 install -r /tmp/requirements.txt && \
    rm /etc/nginx/sites-enabled/default && \
    rm -r /root/.cache

# Create nginx user
RUN useradd nginx

# Copy the Nginx global conf
COPY nginx.conf /etc/nginx/

# Copy the Flask Nginx site conf
COPY flask-site-nginx.conf /etc/nginx/conf.d/

# Copy the base uWSGI ini file to enable default dynamic uwsgi process number
COPY uwsgi.ini /etc/uwsgi/

# Custom Supervisord config
COPY supervisord.conf /etc/supervisord.conf

# Add demo masterdataapi
COPY ./masterdataapi /app
WORKDIR /app

EXPOSE 80

CMD ["/usr/bin/supervisord"]
