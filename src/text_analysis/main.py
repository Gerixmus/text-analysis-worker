from text_analysis.summarize import summarize

text: str = input()
summary = summarize(text)
print(summary)