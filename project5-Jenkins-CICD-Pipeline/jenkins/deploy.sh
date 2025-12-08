#! /bin/bash

echo "Deploying to Openshift..."

oc set image dc/demo-app demo-app=$REGISTRY/$IMAGE:$TAG
oc rollout restart dc/demo-app
