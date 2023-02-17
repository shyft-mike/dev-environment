#!/bin/bash

echo "...building api"
docker build -t dev-api . --progress=plain $@