FROM python:3.6-alpine3.6

WORKDIR /var/lib/python3

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
