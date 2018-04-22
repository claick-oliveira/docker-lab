FROM python

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["--bind", "0.0.0.0:8000", "wsgi"]
ENTRYPOINT [ "gunicorn"]