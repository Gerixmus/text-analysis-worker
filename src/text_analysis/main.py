from text_analysis.summarize import Summarizer
from google.cloud import storage
import time
from fastapi import FastAPI
from pydantic import BaseModel

class SummaryRequest(BaseModel):
    input_file: str
    output_file: str

model_start = time.perf_counter()
summarizer = Summarizer("google-t5/t5-small")
model_end = time.perf_counter()
print(f"Model load time: {model_end-model_start:4f}")

app = FastAPI()
client  = storage.Client(project="text-analysis-465423")
bucket = client.bucket("text-analysis-input")

@app.post("/summarize")
def summarize_file(request: SummaryRequest):
    input_blob = bucket.blob(request.input_file)

    with input_blob.open("r", encoding="utf-8") as f:
        text = str(f.read())
        summarize_start = time.perf_counter()
        output = summarizer.summarize(text)
        summarize_end = time.perf_counter()
        print(f"Summarize time: {summarize_end-summarize_start:4f}")

    output_blob = bucket.blob(request.output_file)
    output_blob.upload_from_string(output)

    return { "summary": output }
