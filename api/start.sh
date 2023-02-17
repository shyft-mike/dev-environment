#!/bin/bash

NAME=$1

if [ -z "$1" ]
then
    NAME=dev-api-1
fi

echo "...running api"
docker run -it --name $NAME --rm \
    --volume "/$(pwd)/src":/opt/app/src \
    --net=host dev-api:latest \
    bash

