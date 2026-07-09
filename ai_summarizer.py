from transformers import pipeline as pl
summarizer = pl("summarization")

def ai_summarizer(text):
    if len(text)<100:
        return text
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']
