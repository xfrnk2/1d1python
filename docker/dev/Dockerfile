FROM python:3.10.4

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN mkdir /app
WORKDIR /app

COPY ./ /app/

RUN pip install -r requirements.txt
RUN pip install -r requirements-test.txt
