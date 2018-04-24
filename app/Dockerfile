FROM python

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["--bind", "0.0.0.0:8000", "wsgi"]

ENTRYPOINT [ "gunicorn"]