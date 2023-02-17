#!/bin/bash

NAME=$1

if [ -z "$1" ]
then
    NAME=dev-server-1
fi

echo "...running server"
docker run --name $NAME -d -p 8888:80 dev-server:latest
    

