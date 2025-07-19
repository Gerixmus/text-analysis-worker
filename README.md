# Text Analysis Service

This service processes input text files stored in a Google Cloud Storage bucket and generates summarized output using a transformer-based model (`google-t5/t5-small`). The summarized result is then uploaded back to the same bucket.

## Setup

Provide the path to the folder containing you local ADC file as `GCLOUD_CONFIG_PATH` environment variable.