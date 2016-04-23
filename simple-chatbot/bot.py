import aiml
import os

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
#kernel.learn("std-startup.xml")

data_location = "./"


#kernel.learn("./data/bot.aiml")

files = [f for f in os.listdir(data_location) if f.endswith('.aiml')]
for f in files:
    kernel.learn(data_location + f)
    #print f

#os.system('cls')
print(chr(27) + "[2J")
#kernel.respond("load aiml b")  

# Press CTRL-C to break this loop
while True:
    print kernel.respond(raw_input("Enter your message >> "))
