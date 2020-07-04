import os

import PyPDF2

pdfFiles = []
for filename in os.listdir("."):
    if filename.endswith(".pdf"):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

print(pdfFiles)
