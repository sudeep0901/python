# sudo apt-get install portaudio19-dev python-pyaudio python3-pyaudio

import speech_recognition as sr

r = sr.Recognizer()
print(sr.Microphone.list_microphone_names())
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)  # here
    print("say Something")
    audio = r.listen(source,timeout=10, phrase_time_limit=10)
    print("time over thanks")

try:
    print("TEXT:" + r.recognize_google(audio))
except:
    pass;

# Set properties _before_ you add things to say

# sudo apt-get update && sudo apt-get install espeak

# sudo apt-get install espeak

text = """Swami Vivekananda (Bengali: [ʃami bibekanɔndo] (About this soundlisten); 12 January 1863 – 4 July 1902), born Narendranath Datta (Bengali: [nɔrendronatʰ dɔto]), was an Indian Hindu monk, a chief disciple of the 19th-century Indian mystic Ramakrishna.[4][5] He was a key figure in the introduction of the Indian philosophies of Vedanta and Yoga to the Western world[6][7] and is credited with raising interfaith awareness, bringing Hinduism to the status of a major world religion during the late 19th century.[8] He was a major force in the revival of Hinduism in India, and contributed to the concept of nationalism in colonial India.[9] Vivekananda founded the Ramakrishna Math and the Ramakrishna Mission.[7] He is perhaps best known for his speech which began with the words - "Sisters and brothers of America ...,"[10] in which he introduced Hinduism at the Parliament of the World's Religions in Chicago in 1893.

Born into an aristocratic Bengali Kayastha family of Calcutta, Vivekananda was inclined towards spirituality. He was influenced by his guru, Ramakrishna, from whom he learnt that all living beings were an embodiment of the divine self; therefore, service to God could be rendered by service to humankind. After Ramakrishna's death, Vivekananda toured the Indian subcontinent extensively and acquired first-hand knowledge of the conditions prevailing in British India. He later travelled to the United States, representing India at the 1893 Parliament of the World's Religions. Vivekananda conducted hundreds of public and private lectures and classes, disseminating tenets of Hindu philosophy in the United States, England and Europe. In India, Vivekananda is regarded as a patriotic saint, and his birthday is celebrated as National Youth Day."""
import pyttsx3
engine = pyttsx3.init()

engine.setProperty('rate', 130)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1
voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
# engine.say("I will speak this text" + r.recognize_google(audio))

en_voice_id = "hindi"

# Use female English voice
engine.setProperty('voice', en_voice_id)
engine.say('Hello with my new voice')
engine.say(text)
engine.runAndWait()

# from gtts import gTTS
# import os
# tts = gTTS(text='Good morning', lang='en')
# tts.save("good.mp3")
# os.system("mpg321 good.mp3")