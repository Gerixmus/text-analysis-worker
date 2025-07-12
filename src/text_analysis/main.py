from text_analysis.summarize import Summarizer
from pathlib import Path
import argparse
from google.cloud import storage

def main():
    client  = storage.Client(project="text-analysis-465423")
    bucket = client.bucket("text-analysis-input")

    summarizer = Summarizer("facebook/bart-large-cnn")

    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="input_blob_name", required=True, help="Blob name")
    parser.add_argument("--out", dest="output_blob_name", required=True, help="Blob name")
    args = parser.parse_args()

    input_blob_name = args.input_blob_name
    input_blob = bucket.blob(input_blob_name)

    with input_blob.open("r", encoding="utf-8") as f:
        text = str(f.read())
        output = summarizer.summarize(text)

    output_blob_name = args.output_blob_name
    output_blob = bucket.blob(output_blob_name)

    output_blob.upload_from_string(output)

if __name__ == "__main__":
    main()