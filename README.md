These 3 files demonstrate my tinkering around with winsound in a Python environment. This was tested on Windows 7 where the playback was flawless. 

I've had some clipping issues in Windows 10. I don't believe this will work on Linux/Mac unless you can find a way to install or run 'winsound'.

########################
cascadingTriads.py was my first experimentation with winsounds. I decided to iterate through a C Major arpeggio ascending and then descending. To do this I had to map out a suitable range of notes from the C Major scale. I settled on the range C4-C7, picking only C E G at various octaves. 10 notes gave me a wide enough range that was both interesting yet pleasant.

I did the same for G Minor to provide a contrast. The ascending and descending iterations would consist of of 8 permutations of 4 notes. For example the first 3 iterations would be:

C E G C
E G C E
G C E G

I'd make sure the start and end interval landed on the right notes and avoid any out of bounds errors.

The descendingTriad function is very similar except it decrements and printsat an offset to go back in the iteration.

I have various finale endings commented out at the end that feature prolonged bass and higher pitched notes. You can play around with whatever ending may suit you.

My default iteration for this is calling ascending and descending twice followed by the James Bond ending.

We'll ascend in G Minor, descend in C Major, ascend back in C Major, descend in Gminor, before finishing with the grand Bond finale chord.
########################



########################
"arpeggiatedMoonlight.py" is my streamlined  code for a Moonlight Sonata demo. 

I created variables for all notes involved, lists of chords containing relevant variables, and then lists of measures containing the relevant chords.

The arpeggiate function takes a chord progression list, and the number of permutations for each chord in the list.

As with my rhythm limitations from the first demo attempt, I didn't develop the ability to permutate each chord within the chord progression its own amount of times.

Each chord will permutate the same as the rest in the progression list.

This version features involved console printing that will tell you the number of chords per progression, the chord position in the current sequence, and the amount of times the chord has been repeated in the sequence. Feel free to comment them out if you get a headache.

At the end I call 3 instances of the arpeggiate function, each taking a different list of chord progressions and repeating the chords x amount of times.

The end result is the first 30 seconds or so of the left hand of Beethoven's 1st Movement of Moonlight Sonata.
########################


########################
oldSpaghettiLoopArpeggio.py was my first attempt at recreating part of Beethoven's Moonlight Sonata. It consists of two test runs:

The first features every note plays from one looped list at 250 speed.

The second features each permutation broken up into variables and then iterated through a for loop x amount of times.

The playback is strictly monophonic, and for demo purposes, I left the speed the same. Though I'm sure future enhancements can include more elaborate rhythm construction.
########################