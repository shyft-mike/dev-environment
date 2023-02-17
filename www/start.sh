#!/bin/bash

NAME=$1

if [ -z "$1" ]
then
    NAME=dev-www-1
fi

echo "...running www"
docker run -it --name $NAME --rm \
    --volume "/$(pwd)":/usr/src/www \
    --net=host dev-www:latest \
    sh

