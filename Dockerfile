FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.8

COPY requirements.txt /app/app/requirements.txt

RUN pip3 install -r /app/app/requirements.txt

COPY ./app /app

RUN mkdir -p /app/app/modules/report
RUN mkdir -p /app/app/static
RUN chmod 755 /app/app/static
RUN touch /app/app/static/index.html

CMD ["/usr/bin/supervisord"]
