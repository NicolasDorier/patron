FROM python:3.7.1-alpine3.8

WORKDIR /patron

COPY . /patron

RUN apk add --no-cache gcc musl-dev libffi libffi-dev python3-dev openssl-dev tzdata
RUN ln -sf /usr/share/zoneinfo/Universal /etc/localtime
RUN pip install gunicorn
RUN pip install -r requirements.txt
RUN chmod +x boot.sh

ENV FLASK_APP=patron.py
ENV TZ=Universal
ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:8006 --workers=3 --access-logfile=- --error-logfile=-"

EXPOSE 8006

ENTRYPOINT ["./boot.sh"]
