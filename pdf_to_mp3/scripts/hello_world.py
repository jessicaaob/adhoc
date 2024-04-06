import pyttsx3, PyPDF2

text = 'Hello World'
speaker = pyttsx3.init()

speaker.save_to_file(text, "test.WAV")
speaker.say(text)
speaker.runAndWait()

speaker.stop()