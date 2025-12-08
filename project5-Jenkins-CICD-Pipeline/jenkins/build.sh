#! /bin/bash

echo "Building Docker Image ..."
docker build -t $REGISTRY/$IMAGE:$TAG ./app

