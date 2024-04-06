# taken from https://www.youtube.com/watch?v=LXsdt6RMNfY
# NOTES:  file in ../references/notes.tct

import pyttsx3, PyPDF2
import wave

pdfreader = PyPDF2.PdfReader(open('../data/external/Accenture-Life-Trends-2024-Report.pdf', 'rb'))
speaker = pyttsx3.init()

clean_text = ''
for page_num in range(len(pdfreader.pages)):
    #text = pdfreader.getPage(page_num).extract_text()
    text = pdfreader.pages[page_num].extract_text()
    clean_text += text.strip().replace('\n', ' ')
print('PDF text loaded and cleaned')

speaker.save_to_file(clean_text, 'life_trends.wav')
speaker.runAndWait()

speaker.stop()

audio = open("life_trends.wav", 'rb').read()
params = (2, 2, 44100, 0, 'NONE', 'not compressed')

with wave.open("life_trends_saved.wav", 'wb') as audio_file:
    audio_file.setparams(params)
    audio_file.writeframes(audio)

