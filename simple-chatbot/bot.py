import aiml
import os

sessionId = 1

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
#kernel.learn("std-startup.xml")

sessionData = kernel.getSessionData(sessionId)

data_location = "./data/"


brain_location = "./data/brain_files/bot_brain.brn"

if os.path.isfile(brain_location):
    kernel.bootstrap(brainFile = brain_location)
else:
	files = [f for f in os.listdir(data_location) if f.endswith('.aiml')]
	for f in files:
		kernel.learn(data_location + f)

	kernel.saveBrain(brain_location)


# Press CTRL-C to break this loop
while True:
	message = raw_input("Enter your message >> ")
	if(message == "exit()"):
		print "See you later!"
		exit()

	print kernel.respond(message)
