import random



# Naturals. If the dictionary returns -1, try either the sharps or flats.

NaturalsToInt = {
		"C" 	: 	0,
		"C#" 	: 	-1,
		"Db" 	: 	-1,
		"D" 	: 	2,
		"D#" 	: 	-1,
		"Eb" 	: 	-1,
		"E" 	: 	4,
		"E#"	:	-1,
		"Fb" 	: 	-1,
		"F" 	: 	5,
		"F#" 	: 	-1,
		"Gb" 	: 	-1,
		"G"  	: 	7,
		"G#" 	: 	-1,
		"Ab" 	: 	-1,
		"A" 	:	9,
		"A#" 	: 	-1,
		"Bb" 	: 	-1,
		"B"		: 	11,
		"B#"	:	-1,
		"Cb"	: 	-1
	}
	
IntToNaturals = dict((reversed(item) for item in NaturalsToInt.items()))


# "All pitch" dictionaries for flexible user input

SharpsToInt = {
		"C" 	: 	-1,
		"C#" 	: 	1,
		"Db" 	: 	-1,
		"D" 	: 	-1,
		"D#" 	: 	3,
		"Eb" 	: 	-1,
		"E" 	: 	-1,
		"E#"	:	5,
		"Fb" 	: 	-1,
		"F" 	: 	-1,
		"F#" 	: 	6,
		"Gb" 	: 	-1,
		"G"  	: 	-1,
		"G#" 	: 	8,
		"Ab" 	: 	-1,
		"A" 	:	-1,
		"A#" 	: 	10,
		"Bb" 	: 	-1,
		"B"		: 	-1,
		"B#"	:	0,
		"Cb"	: 	-1
	}
	
IntToSharps = dict((reversed(item) for item in SharpsToInt.items()))


FlatsToInt = {
		"C" 	: 	-1,
		"C#" 	: 	-1,
		"Db" 	: 	1,
		"D" 	: 	-1,
		"D#" 	: 	-1,
		"Eb" 	: 	3,
		"E" 	: 	-1,
		"Fb" 	: 	4,
		"F" 	: 	-1,
		"F#" 	: 	-1,
		"Gb" 	: 	6,
		"G"  	: 	-1,
		"G#" 	: 	-1,
		"Ab" 	: 	8,
		"A" 	:	-1,
		"A#" 	: 	-1,
		"Bb" 	: 	10,
		"B"		: 	-1,
		"Cb"	: 	11
	}

IntToFlat = dict((reversed(item) for item in FlatsToInt.items()))


	
IntervalToInt = {
	"m2"	:	1,
	"M2"	:	2,
	"m3"	:	3,
	"M3"	:	4,
	"P4"	:	5,
	"TT"	:	6,
	"P5"	:	7,
	"m6"	:	8,
	"M6"	:	9,
	"m7"	:	10,
	"M7"	:	11,
	"P8"	:	12
	}

IntToInterval = dict((reversed(item) for item in IntervalToInt.items()))
	
	
#-----Functions----


def PitchToInt(pitchstr):
	#TODO parameters for whether to use sharps or flats... Sense of scale?
	pitchint = NaturalsToInt.get(pitchstr)
	if pitchint == -1:
		pitchint = SharpsToInt.get(pitchstr)
	if pitchint == -1:
		pitchint = FlatsToInt.get(pitchstr)
	return pitchint


def IntToPitch(pitchint):
	#TODO parameters for whether to use sharps or flats... Sense of scale?
	pitchstr = IntToNaturals.get(pitchint)
	if pitchstr == None:
		pitchstr = IntToSharps.get(pitchint)
	if pitchstr == None:
		pitchstr = IntToFlats.get(pitchint)
	return pitchstr






#-----Main---------




idifficulty = 0;
input_note = 0
iterations = 3;
	
#print("Input: " + pitches[input_note])
#print("Iterations: " + str(iterations))

#iterations = input("How many intervals per note? ")





print("\nStarting on " + IntToPitch(input_note) + ";")

for i in range(0,iterations):
	interval = random.randint(1,12)
	direction = random.randint(0,1)
	dirstr = "up"
	if (not direction): 
		direction = -1
		dirstr = "down"	
	print("\tGo one " + IntToInterval.get(interval) + " " + dirstr + ";")
	input_note = input_note + direction * interval
	
input_note = input_note % 12
	
print("\nWhat is the new note?")
print("(Hint, it's " + IntToPitch(input_note) + ")")

		
	



