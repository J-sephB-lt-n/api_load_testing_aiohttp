
```bash
$ GCP_PROJ_ID="your GCP project ID"
$ REGION_NAME="region in which to host the cloud run service"
$ API_NAME="test-api"
$ ART_REG_REPO_NAME="your-artifact-registry-repo-name" # this must already exist

# !USER WARNING! This is deployed externally with 0 security
$ source rest_api/deploy_rest_api.sh 
```

```bash
$ CLOUD_RUN_SERVICE_URL="https://test-api-r2389hfdjksbf8932" # get this from the deployed cloud run service
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python run_loadtest.py --service_url "${CLOUD_RUN_SERVICE_URL}"
```


