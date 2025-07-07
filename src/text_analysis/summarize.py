from transformers.pipelines import pipeline

def summarize(text: str):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summarized_text = summarizer(text, max_length = 130, min_length = 30, do_sample = False)
    return(summarized_text[0]['summary_text'])