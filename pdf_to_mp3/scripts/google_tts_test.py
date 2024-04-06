from PyPDF2 import PdfReader
#import pyttsx3
from gtts import gTTS

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text

def convert_text_to_speech(text, output_file):
    tts = gTTS(text)
    tts.save(output_file)

pdf_path = "../data/external/Accenture-Life-Trends-2024-Report.pdf"
all_text = extract_text_from_pdf(pdf_path)
print('text extracted')

output_file = "output.mp3"
print('converting to speech & saveing file...')
convert_text_to_speech(all_text, output_file)