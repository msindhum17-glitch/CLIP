from gtts import gTTS
from IPython.display import Audio,display
text=input("Enter text")
tts=gTTS(text=text,lang="en")
tts.save("speech.mp3")
display(Audio("speech.mp3"))
