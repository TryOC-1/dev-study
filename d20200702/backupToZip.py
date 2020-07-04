import os

import PyPDF2

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir("."):
    if filename.endswith(".pdf"):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF file.
for filename in pdfFiles:
    pdfFileObj = open(filename, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # Loop through all the pages (except the first) and add item.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open("allminutes.pdf", "wb")
pdfWriter.write(pdfOutput)
pdfOutput.close()
