from transformers.pipelines import pipeline

class Summarizer:
    def __init__(self, model: str):
        self.summarizer = pipeline("summarization", model)

    def summarize(self, text: str) -> str:
        summarized_text = self.summarizer(text, max_length = 130, min_length = 30, do_sample = False)
        return(summarized_text[0]['summary_text'])