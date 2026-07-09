from flask import Flask as fl
from flask import render_template as rt
from flask import request as rq 
from summarizer import summarize_text as st
from quiz_generator import genrate_quiz as qz
from flashcard import generate_flashcards as gf
from pdf_export import create_pdf as cp
from flask import send_file
import os
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
app = fl(__name__)
lastest_summary = ""
@app.route('/', methods=['GET', 'POST'])
def home():
    global lastest_summary
    summary = ""
    quiz = []
    flashcards = []
    
    
    if rq.method == 'POST':
        text = rq.form.get('text')
        pdf_file = rq.files.get('pdf_file')
        if pdf_file and pdf_file.filename != '':
            from pdf_reader import extract_text_from_pdf as et
            text = et(pdf_file)
        if text:    
            summary = st(text)
            lastest_summary = summary
            quiz = qz(text)
            flashcards = gf(text)
    return rt('index.html', summary=summary, quiz=quiz, flashcards=flashcards)


@app.route('/download_pdf')
def download():
    cp(lastest_summary,"summary.pdf")
    return send_file('summary.pdf', as_attachment=True)


if __name__ == '__main__':

    app.run(host='0.0.0', port=int(os.environ.get('PORT', 5000)))
        
