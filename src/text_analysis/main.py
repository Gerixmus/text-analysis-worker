from text_analysis.summarize import summarize
from pathlib import Path
import argparse
from google.cloud import storage

def main():
    storage_client = storage.Client(project="text-analysis-465423")
    buckets = storage_client.list_buckets()

    print("Buckets:")
    for bucket in buckets:
        print(bucket.name)

    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="input_path", required=True, help="Path to input text file")
    parser.add_argument("--out", dest="output_path", required=True, help="Path to output text file")
    args = parser.parse_args()

    input_path = Path(args.input_path)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {input_path}")
    
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()
        output = summarize(text)

    output_path = Path(args.output_path)
    with open(output_path, "w") as f:
        f.write(output)

if __name__ == "__main__":
    main()