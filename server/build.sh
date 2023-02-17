#!/bin/bash

echo "...moving web distribution"
mv ../www/dist ./dist

echo "...building server"
docker build -t dev-server . --progress=plain $@