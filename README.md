# Text Analysis Worker

This worker processes input text files stored in a Google Cloud Storage bucket and generates summarized output using a transformer-based model (`facebook/bart-large-cnn`). The summarized result is then uploaded back to the same bucket.