import PyPDF2 as pdf
def extract_text_from_pdf(pdf_file):
    text=""
    reader=pdf.PdfReader(pdf_file)
    for page in reader.pages:
        text+=page.extract_text()
    return text
