from text_analysis.summarize import summarize
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="text file you want to summarize")
args = parser.parse_args()

f = open(args.file)

summary = summarize(f.read())
print(summary)