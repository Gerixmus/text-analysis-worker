from transformers.pipelines import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize(text: str) -> str:
    summarized_text = summarizer(text, max_length = 130, min_length = 30, do_sample = False)
    return(summarized_text[0]['summary_text'])