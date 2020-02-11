import winsound
from time import sleep

# Intro to Moonlight Sonata Arpeggios
# Old Spaghetti For Loop Versions

#######################################
# This version features every note plays in one list played at 250 speed

moonlightFull = [415.3,554.37,659.25,415.3,554.37,659.25,415.3,554.37,659.25,415.3,554.37,659.25,440,554.37,659.25,440,554.37,\
659.25,440,554.37,659.25,440,554.37,659.25,440,587.33,739.99,440,587.33,739.99,440,587.33,739.99,440,587.33,739.99,415.3,523.25,\
739.99,415.3,523.25,739.99,415.3,554.37,659.25,415.3,554.37,659.25,415.3,554.37,622.25,415.3,554.37,622.25,369.99,523.25,622.25,369.99,\
523.25,622.25,329.63,415.3,415.3,554.37,659.25,554.37,659.25,830.61,554.37,659.25,830.61]

for note in moonlightFull:
        winsound.Beep(int(note), 250)
        #sleep(0.2)
        # print(note)
#######################################



#######################################
# This version features every chord permutation declared as its own variable then looped over x amount of times

'''
moonlightOne = [415.3,554.37,659.25]
moonlightTwo = [440,554.37,659.25]
moonlightThree = [440,587.33,739.99]
moonlightFour = [415.3,523.25,739.99]
# moonlightFive = [415.3,554.37,659.25]
moonlightSix = [415.3,554.37,622.25]
moonlightSeven = [369.99,523.25,622.25]
moonlightEight = [329.63,415.3,554.37]
moonlightOneInv1 = [554.37,659.25,830.61]
# moonlightOneInv2 = [659.25,830.61,1108.73]


for i in range(4):
	for note in moonlightOne:
		winsound.Beep(int(note), 300)
		sleep(0.30)

for i in range(4):
	for note in moonlightTwo:
		winsound.Beep(int(note), 300)
		sleep(0.3)

for i in range(4):
	for note in moonlightThree:
		winsound.Beep(int(note), 300)
		sleep(0.3)

for i in range(2):
	for note in moonlightFour:
		winsound.Beep(int(note), 300)
		sleep(0.3)

for i in range(2):
	for note in moonlightOne:
		winsound.Beep(int(note), 300)
		sleep(0.3)

for i in range(2):
	for note in moonlightSix:
		winsound.Beep(int(note), 300)
		sleep(0.3)

for i in range(2):
	for note in moonlightSeven:
		winsound.Beep(int(note), 300)
		sleep(0.3)

for i in range(1):
	for note in moonlightEight:
		winsound.Beep(int(note), 300)
		sleep(0.3)

for i in range(1):
	for note in moonlightOne:
		winsound.Beep(int(note), 300)
		sleep(0.3)

for i in range(2):
	for note in moonlightOneInv1:
		winsound.Beep(int(note), 300)
		sleep(0.3)
for i in range(1):
	for note in moonlightOneInv2:
		winsound.Beep(int(note), 300)
	'''
#######################################