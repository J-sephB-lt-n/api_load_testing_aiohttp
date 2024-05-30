#!/bin/bash

cd rest_api/

echo "start time: $(date)"
gcloud config set project $GCP_PROJ_ID
gcloud config set run/region $REGION_NAME

docker_image_name=$REGION_NAME-docker.pkg.dev/$GCP_PROJ_ID/$ART_REG_REPO_NAME/$API_NAME

echo "started build: $(date)"
gcloud builds submit --tag $docker_image_name

echo "started deploy: $(date)"
gcloud run deploy $API_NAME \
    --image $docker_image_name \
    --max-instances 1 \
    --min-instances 0 \
    --allow-unauthenticated \
    --timeout 60 \
    --ingress all

echo "finished: $(date)"

cd ..
