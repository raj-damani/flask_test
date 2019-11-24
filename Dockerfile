FROM ubuntu

RUN apt-get update

RUN apt-get install python3-pip python3-dev nginx

RUN pip3 install flask gunicorn

RUN pip3 install WTForms

COPY flaskblog.py /flaskblog.py

RUN chmod 755 /flaskblog.py

CMD ./flaskblog.py

