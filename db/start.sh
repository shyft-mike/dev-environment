#!/bin/bash

NAME=$1

if [ -z "$1" ]
then
    NAME=dev-db-1
fi

echo "...running db"
docker run -it --name $NAME --rm \
    --volume "/$(pwd)/data":/opt/app/src \
    --net=host dev-db:latest \
    bash

