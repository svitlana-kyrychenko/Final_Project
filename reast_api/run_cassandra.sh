#!/bin/bash

docker run --name cassandra-server --network kafka-network -p 9042:9042 -d cassandra:2.2.19
sleep 90
docker cp ./ddl-script.cql cassandra-server:/
docker exec -it cassandra-server cqlsh -f ddl-script.cql
