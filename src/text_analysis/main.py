from text_analysis.summarize import summarize
from pathlib import Path
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="input_path", required=True, help="Path to input text file")
    args = parser.parse_args()

    input_path = Path(args.input_path)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {input_path}")
    
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()
        output = summarize(text)
    
    print(output)

if __name__ == "__main__":
    main()