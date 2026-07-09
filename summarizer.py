from nltk.tokenize import sent_tokenize
def summarize_text(text):
    sentences = sent_tokenize(text)
    if len(sentences) <= 3:
        return text
    return ' '.join(sentences[:3]) 
