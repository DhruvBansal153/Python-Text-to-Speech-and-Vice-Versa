# importing the modules 
import PyPDF2 
import pyttsx3 

# path of the PDF file 
path = open('Twinkle.pdf', 'rb') 

# creating a PdfReader object 
reader = PyPDF2.PdfReader(path) 

# the pages with which you want to start 
# this will read the page 0. You can add more pages in list. 
from_page = reader.pages[0] 

# extracting the text from the PDF 
text = from_page.extract_text() 

# reading the text 
speak = pyttsx3.init() 
speak.say(text) 
speak.runAndWait()