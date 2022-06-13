FROM python:3.9-slim

WORKDIR /rest_api

COPY ./reast_api/requirements.txt /rest_api
COPY ./reast_api/src/ /rest_api

RUN pip install --upgrade pip
RUN pip install  -r requirements.txt

ENTRYPOINT ["python", "rest_api.py"]
