#!/bin/bash

echo "...building db"
docker build -t dev-db . --progress=plain $@