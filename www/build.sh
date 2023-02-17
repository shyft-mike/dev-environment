#!/bin/bash

echo "...building www"
docker build -t dev-www . --progress=plain $@