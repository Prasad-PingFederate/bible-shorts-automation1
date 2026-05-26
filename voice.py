from gtts import gTTS

text = """
Late at night, the disciples were trapped in a violent storm.
Suddenly, a glowing figure appeared walking on water.
The storm stopped instantly.
"""

tts = gTTS(text=text)

tts.save("voice.mp3")

print("Voice Generated")