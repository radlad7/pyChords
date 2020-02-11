import winsound
from time import sleep

# Declare notes as frequency doubles
Gsharp4 = 415.3
Csharp5 = 554.37
E5 = 659.25
A5 =  440
D5  = 587.33
Fsharp5 = 739.99
C5 = 523.25
Dsharp5 = 622.25
Fsharp4 = 369.99
E4 = 329.63
Gsharp5 = 830.61

# Aggregate notes into chords
chord1 = [Gsharp4, Csharp5, E5]
chord2 = [A5, Csharp5, E5]
chord3 = [A5, D5, Fsharp5]
chord4 = [Gsharp4, C5, Fsharp5]
chord5 = [Gsharp4, Csharp5, Dsharp5]
chord6 = [Fsharp4, C5, Dsharp5]
chord7 = [E4, Gsharp4, Csharp5]
chord_8_1FirstInv = [Csharp5, E5, Gsharp5]

# Aggregate chords into measures
moonlightIntro = [chord1, chord2, chord3]
moonlightIntro2 = [chord4, chord1, chord5, chord6]
moonlightIntro3 = [chord7, chord1, chord_8_1FirstInv, chord_8_1FirstInv]

# Arpeggiate function will take a progression (list of chords) and number of durations for each chord in progression (repeatChord)
# Currently repeatChord affects the entire progression, thus each set is locked into the same permutations
def arpeggiate(progression, repeatChord = 0):
        measures = len(progression)
        print("Total # of Chords in progression: " + str(measures))
        repeatCount = 0
        chordCount = 1

        while chordCount < measures:
                for chord in progression:
                        print("Chord position in sequence: " + str(chordCount))
                        while repeatCount < repeatChord:
                                for note in chord:
                                        winsound.Beep(int(note), 350)
                                        print(note)
                                repeatCount += 1
                                print("Chord repeated: " + str(repeatCount))
                        chordCount += 1
                        repeatCount = 0

                
# play intro1 4x each
arpeggiate(moonlightIntro, 4)
# play intro2 2x each
arpeggiate(moonlightIntro2, 2)
# play intro3 1x
arpeggiate(moonlightIntro3, 1)