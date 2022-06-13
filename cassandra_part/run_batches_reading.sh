docker build -f Dockerfile.kafka -t from-kafka .
docker run --rm --network kafka-network -v --rm from-kafka --name batches-kafka