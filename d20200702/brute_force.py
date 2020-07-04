import PyPDF2

password = []

with open("dictionary.txt") as f:
    passwords = f.read().split("\n")

pdfReader = PyPDF2.PdfFileReader("encrypytedminutes.pdf", "rb")

for password in passwords:
    pdfReader = PyPDF2.PdfFileReader("encrypytedminutes.pdf", "rb")
    pdfReader.decrypt(password)
    print(password)
    try:
        pageObj = pdfReader.getPage(0)
        print(f"decrypted!! password is '{password}'")
        break
    except PyPDF2.utils.PdfReadError:
        pass
