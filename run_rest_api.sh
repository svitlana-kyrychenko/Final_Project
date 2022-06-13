docker build -f ./reast_api/Dockerfile.app -t rest_api .
docker run -p 8080:8080 --rm --network kafka-network -v --rm rest_api --name rest
