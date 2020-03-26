import music21 as m21
import random

class pentatonicScale:
	def __init__(self, note, scale_name):
		# Specify any desired pentatonic scales here by adding all non-root notes as intervals.
		self.major = ['M2','M3','p5','M6']
		self.minor = ['m3','p4','p5','m7']
		self.dominant = ['M2','M3','p5','m7']
		self.dorian = ['M2','m3','p5','M6']

		self.scale = self.getScale(note, scale_name)
		self.name = note + " " + scale_name
		
	def getScale(self, note_name, scale_name):
		# Returns a scale based on the given string representing a pitch and given scale type.
		note_name = note_name.replace(" ", "") # Remove spaces
		scale_name = scale_name.replace(" ", "").lower()

		if len(note_name) == 2 and note_name[1] == 'b': # Fix flats.
			note_name = note_name[0] + '-'

		scale_intervals = []

		if scale_name == "major":
			scale_intervals = self.major
		elif scale_name == "maj":
			scale_intervals = self.major
		elif scale_name == "minor":
			scale_intervals = self.minor
		elif scale_name == "min":
			scale_intervals = self.minor
		elif scale_name == "dom":
			scale_intervals = self.dominant
		elif scale_name == "dominant":
			scale_intervals = self.dominant
		elif scale_name == "dorian":
			scale_intervals = self.dorian

		intervals = [m21.interval.Interval(x) for x in scale_intervals]

		pitch = m21.pitch.Pitch(note_name)
		pitch.octave = 4
		scale = [pitch]
		for i in intervals:
			scale.append(i.transposePitch(pitch))

		stream = m21.stream.Stream() # Show the scale.
		for p in scale:
			note = m21.note.Note(p, quarterLength=0.5)
			stream.append(note)
		stream.show()

		return scale

	def generateCellPattern(self, cell_length, num_cells, direction=""):
		# Generates a random pentatonic cell shape and extends it randomly up or down.
		# Input 'up' or 'down' for direction to specify any preference.

		if cell_length > len(self.scale): # Don't allow duplicate notes in the cell, for now.
			print("Cannot generate such a cell! Please try with a shorter cell length.")
			return None

		cell_index = []
		while len(cell_index) < cell_length: # Generate random number, add to cell if it's not already in.
			r = random.randint(0,len(self.scale)-1)
			if r not in cell_index:
				cell_index.append(r)

		print(cell_index)

		output_pattern_indices = []
		if random.randint(0,1):	# Ascending
			print("Ascending")
			for cell in range(num_cells):
				output_pattern_indices = output_pattern_indices + cell_index
				cell_index = [i+1 for i in cell_index] # Increment each index.
		else:					# Descending
			print("Descending")
			for cell in range(num_cells):
				output_pattern_indices = output_pattern_indices + cell_index
				cell_index = [i-1 for i in cell_index] # Increment each index.

		stream = m21.stream.Stream()
		cell_diff = 0
		for i in output_pattern_indices:
			# We need to transpose notes independently and as a cell.
			# if i % cell_length == 0: # Start of a cell.
			# 	cell_diff = 0
			# 	while i >= len(self.scale):
			# 		i -= len(self.scale)
			# 		cell_diff += 1
			# 	while i < 0:
			# 		i += len(self.scale)
			# 		cell_diff -= 1

			# else:

			# 	pitch = self.scale[i%len(self.scale)]
			# 	pitch.octave = pitch.octave + octave_diff

			# 	note = m21.note.Note(pitch, quarterLength=0.5)
			# 	stream.append(note)

	# Needs major revision still! Think about the problem with a few example licks and precise octaves.
		stream.show()

def main():
	gen = pentatonicScale('G','maj')
	scale = gen.scale
	gen.generateCellPattern(4,4)

if __name__ == "__main__":
	main()