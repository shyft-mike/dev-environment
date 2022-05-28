#!/bin/bash

NAME=$1

if [ -z "$1" ]
then
    NAME=dev-env-1
fi

echo "-----Running-----"
docker run -it --name $NAME --rm \
    --volume "/$(pwd)/python":/root/dev \
    --net=host dev-env:latest \
    bash