from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import textwrap


def to_pdf(str):
    pdf_file = "summary.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.setFont("Helvetica", 12)
    wrapped_text = textwrap.wrap(str, width=70) 
    y_position = 750
    for line in wrapped_text:
        c.drawString(100, y_position, line)
        y_position -= 14
    c.save()
    print("PDF created and string written to it.")