FROM pypy
RUN mkdir -p /usr/api/logs
WORKDIR /usr/api
RUN apt-get update && apt-get --allow-unauthenticated install -y supervisor
RUN mkdir -p /var/log/supervisor
COPY ./deployment/gunicorn.conf /etc/supervisor/conf.d/supervisord.conf
COPY . /usr/api
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 4100
VOLUME /usr/api
CMD ["/usr/bin/supervisord"]