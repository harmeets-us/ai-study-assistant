from reportlab.pdfgen import canvas
from textwrap import wrap

def create_pdf(text, filename):
    c = canvas.Canvas(filename)

    y = 800

    lines = wrap(text, width=80)

    for line in lines:
        c.drawString(50, y, line)
        y -= 20

        if y < 50:
            c.showPage()
            y = 800

    c.save()