#!/bin/bash

echo "-----Building-----"
docker build -t dev-env .

echo "-----Running-----"
docker run -it --name dev-env-1 --rm \
    --volume "/$(pwd)/python":/root/dev \
    --net=host dev-env:latest \
    sh