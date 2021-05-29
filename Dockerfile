# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3.7-buster

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log

# install dos2unix
RUN apt-get update && apt-get install -y dos2unix

# copy source and install dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/cactugram
COPY requirements.txt start-server.sh /opt/app/
COPY .pip_cache /opt/app/pip_cache/
COPY . /opt/app/cactugram/
WORKDIR /opt/app
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app

RUN dos2unix /opt/app/start-server.sh && apt-get --purge remove -y dos2unix && rm -rf /var/lib/apt/lists/*

# start server
EXPOSE 8029
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]
