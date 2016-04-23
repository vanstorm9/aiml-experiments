import aiml
import os

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
    print kernel.respond(raw_input("Enter your message >> "))
