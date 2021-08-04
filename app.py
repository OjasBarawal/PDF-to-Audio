import PyPDF2
import pyttsx3

# path to pdf
path = open('example.pdf', 'rb')

# creating a pdf-file-reader object
pdfReader = PyPDF2.PdfFileReader(path)

# the page with which you want to start
from_page = pdfReader.getPage(1)

# Extracting the text from pdf
text = from_page.extractText()

# reading the text
speak = pyttsx3.init()
speak.setProperty('rate', 150)
speak.say(text)
speak.runAndWait()
