import PyPDF2
pdfFileObj = open("E:/Resume/Resume-Research-Anush-Gupta MLH.pdf", 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
pageObj = pdfReader.pages[0].extract_text()
print(pageObj)
print(pageObj.extractText())
pdfFileObj.close()