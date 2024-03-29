# text_to_speech_tk.py
import tkinter as tk
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice to an English voice with a British accent
voices = engine.getProperty('voices')
for voice in voices:
    if 'english' in voice.name.lower() and 'uk' in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

# Function to convert text to speech
def convert_text_to_speech():
    text = text_entry.get("1.0", "end-1c")
    rate = rate_scale.get()
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.save_to_file(text, 'output.wav')
    engine.runAndWait()
    engine.stop()

# Create the Tkinter window
window = tk.Tk()
window.title("Text-to-Speech")

# Create the text entry box
text_entry = tk.Text(window, height=10, width=50)
text_entry.pack()

# Create the rate scale
rate_scale = tk.Scale(window, from_=50, to=300, orient=tk.HORIZONTAL, label="Speech Rate")
rate_scale.pack()

# Create the convert button
convert_button = tk.Button(window, text="Convert to Speech", command=convert_text_to_speech)
convert_button.pack()

# Run the Tkinter event loop
window.mainloop()