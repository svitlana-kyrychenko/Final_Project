FROM python:3.9-slim

WORKDIR /cassandra_rest_api

COPY ./cassandra_part/requirements.txt /cassandra_rest_api
COPY ./cassandra_part/src/ /cassandra_rest_api

RUN pip install --upgrade pip
RUN pip install  -r requirements.txt

ENTRYPOINT ["python", "rest_api.py"]
