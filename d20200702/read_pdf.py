import PyPDF2

pdfFileObj = open("meetingminutes.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print("pdfReader.numPages".center(30, "*"))
print(pdfReader.numPages)

print("get page : 0".center(30, "*"))
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
