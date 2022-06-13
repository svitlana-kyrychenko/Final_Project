FROM python:3.9-slim

WORKDIR /streaming

COPY ./requirements.txt /streaming
COPY ./src/reading_stream.py  /streaming

RUN pip install --upgrade pip
RUN pip install  -r requirements.txt

ENTRYPOINT ["python", "reading_stream.py"]
