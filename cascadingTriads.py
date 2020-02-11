import winsound
import time


def ascendingTriad(triadIntervals):
	startInterval = 0
	endInterval = 4
	print(startInterval +1, endInterval -1)
	
	# 8 Permutations of Ascending Triads from list of 10
	for i in range(7):
		for note in triadIntervals[startInterval:endInterval]:
			winsound.Beep(int(note), 250)
		startInterval += 1
		endInterval += 1
		print(startInterval +1, endInterval -1)

def descendingTriad(triadIntervals):
	# Set interval counts to start from end of array in 4 note clusters
	startInterval = -1
	endInterval = -5

	# 8 Permutations of Descending Triads from list of 10
	for i in range(7):
		for note in triadIntervals[startInterval:endInterval:-1]:
			# print(note)
			winsound.Beep(int(note), 250)
		startInterval -= 1
		endInterval -= 1
		print(startInterval +9, endInterval +15)

def bondEnding(chord):
	for i, note in enumerate(chord):
		if i == len(chord) -1:
			winsound.Beep(int(note), 1000)
			# print("BOND CHORD")
		# print(i, note)
		winsound.Beep(int(note), 100)


# Cascading C Major and G Minor Triad Arpeggios in 4 note clusters
# 10 notes per Triad range
c4to7Triad = [261.63,329.63,392,523.25,659.25,783.99,1046.5,1318.51,1567.98,2093]
Gmin4to7Triad = [196,233.08,293.66,392,466.16,587.33,783.99,932.33,1174.66,3135.96]

# James Bond chord - B#4, D5, F#5, A5 - Gmin9
bondChord = [466.16, 587.33, 739.99, 880]

ascendingTriad(Gmin4to7Triad)
descendingTriad(c4to7Triad)
ascendingTriad(c4to7Triad)
descendingTriad(Gmin4to7Triad)
bondEnding(bondChord)

'''
# Various note finale endings
# print("Finale!")
# winsound.Beep(int(Gmin4to7Triad[0]), 3000)

winsound.Beep(int(c4to7Triad[0]), 1500)
winsound.Beep(int(c4to7Triad[1]), 1500)
#winsound.Beep(int(c4to7Triad[2]), 1500)
winsound.Beep(int(c4to7Triad[3]), 1500)
winsound.Beep(int(493.88), 1500) #B4 maj7th
winsound.Beep(int(587.33), 3000) #D5 9th
#winsound.Beep(int(196), 1500) #G3 5th
#winsound.Beep(int(440), 1500) #A4 6th
#winsound.Beep(int(293.66), 1500) #D4 9th
'''