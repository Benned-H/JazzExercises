import music21 as m21

class chordGenerator:
	def __init__(self):
		# Specify any desired chord types here by adding all non-root notes as intervals.
		self.chord_M = ['M3','p5']
		self.chord_m = ['m3','p5']
		self.chord_aug = ['M3','a5']
		self.chord_M7 = ['M3','p5','M7']
		self.chord_m7 = ['m3','p5','m7']
		self.chord_7 = ['M3','p5','m7']
		self.chord_dim7 = ['m3','d5','d7']
		self.chord_M9 = ['M3','p5','M7','M9']
		self.chord_9 = ['M3','p5','m7','M9']

	def getChord(self,chord_name):
		# Performs basic input processing on the given chord.
		new_name = chord_name.replace(" ", "") # Remove spaces

		if len(new_name) == 1:
			return self.getChord_Type(new_name[0:1],"")

		# The note for the chord can either be natural, flat, or sharp.
		if new_name[1] == 'b':
			note_name = new_name[0] + "-" # Music21 names notes using - instead of b for flat.
			return self.getChord_Type(note_name,new_name[2:])
		elif new_name[1] == '#':
			return self.getChord_Type(new_name[0:2],new_name[2:])
		return self.getChord_Type(new_name[0:1],new_name[1:])

	def getChord_Type(self, pitch_str, chord_type):
		# Returns a chord based on the given string representing a pitch and given chord type.
		chord_intervals = []

		sus = False
		# Handle sus chords.
		if len(chord_type) >= 3: # Avoid indexing errors.
			if chord_type[-3:] == 'sus':
				sus = True
				chord_type = chord_type[:-3]

		if chord_type == "":
			chord_intervals = self.chord_M
		elif chord_type == "m":
			chord_intervals = self.chord_m
		elif chord_type == "+":
			chord_intervals = self.chord_aug
		elif chord_type == "M7":
			chord_intervals = self.chord_M7
		elif chord_type == "m7":
			chord_intervals = self.chord_m7
		elif chord_type == "-7":
			chord_intervals = self.chord_m7
		elif chord_type == "7":
			chord_intervals = self.chord_7
		elif chord_type == "dim7":
			chord_intervals = self.chord_dim7
		elif chord_type == "d7":
			chord_intervals = self.chord_dim7
		elif chord_type == "M9":
			chord_intervals = self.chord_M9
		elif chord_type == "9":
			chord_intervals = self.chord_9

		intervals = [m21.interval.Interval(x) for x in chord_intervals]
		if sus:
			for index,interval in enumerate(intervals):
				if interval.simpleName[1] == '3': # Replace thirds with the 11th.
					fourth = m21.interval.Interval("P4")
					intervals[index] = fourth
					break

		pitch = m21.pitch.Pitch(pitch_str)
		pitches = [pitch]
		for i in intervals:
			pitches.append(i.transposePitch(pitch))

		return m21.chord.Chord(pitches)

def main():

	print("Hello"[-3:])

	generator = chordGenerator()
	test_chords = ['CM7','F-7','C9','Bbd7','FM9','C#7sus']
	for chord in test_chords:
		print(chord, generator.getChord(chord))

if __name__ == "__main__":
	main()