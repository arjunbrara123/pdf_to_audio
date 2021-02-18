# importing all the required modules
import PyPDF2
import pyttsx3

# Set up voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Create text to voice function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# creating a pdf object
file = open("sample.pdf", 'rb')
fileReader = PyPDF2.PdfFileReader(file)
obj=PyPDF2.pdf.PageObject(fileReader)

#Read lines out loud
for page in range(fileReader.numPages):
    speak(fileReader.getPage(page).extractText())
