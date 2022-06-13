docker build . -t reading_app
docker run --rm --network kafka-network --rm reading_app