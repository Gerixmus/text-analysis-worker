FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN python -c "from transformers import pipeline; pipeline('summarization', model='facebook/bart-large-cnn')"

COPY . .

ENV PYTHONPATH=/app/src

ENTRYPOINT ["python3", "-m", "text_analysis.main"]