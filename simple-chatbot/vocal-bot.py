import aiml
import os

import pyttsx
import warnings

warnings.simplefilter("ignore")

def text_to_speech(speech):
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    engine.setProperty('rate', rate-50)
    engine.setProperty('volume', volume+2)
    engine.say(speech)
    voices = engine.getProperty('voices')
    engine.runAndWait()



# Create the kernel and learn AIML files
kernel = aiml.Kernel()
#kernel.learn("std-startup.xml")

data_location = "./data/"

files = [f for f in os.listdir(data_location) if f.endswith('.aiml')]
for f in files:
    kernel.learn(data_location + f)
    print f


print(chr(27) + "[2J") # To clear terminal

# Press CTRL-C to break this loop
while True:
    user_input = raw_input("Enter your message >> ")
    response =  kernel.respond(user_input)
    print response
    text_to_speech(response)
