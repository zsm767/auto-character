from random import *

class NameGenerator:
	rFlag = 'G'
	
	generic_firstnames = ['Greg','Samuel','Mark','Tom','Timothy',
	'Harold','John','Todd','Ken','Craig',]
	
	generic_lastnames = ['Johnson','Wordsworth','Frank','Doe','Smith'
	,'Appleton','Smallpox','Wilson','Long','Short',]

	# specific dicts (maybe can just use lists, since accessing times aren't an issue...
	# for races
	#----------------------------------------------------------------#

	human_firstnames = []
	human_lastnames = []

	#----------------------------------------------------------------#

	elf_firstnames = ['Aust', 'Adra', 'Berrian', 'Birel', 'Carric', 'Caelynn', 'Erevan', 'Felosial', 'Ivellion', 'Quarion', 'Lia',
	'Varis', 'Xanathi']
	elf_lastnames = ['Amakiir', 'Amastacia', 'Galanodel', 'Holion', 'Liadon', 'Meliamne', 'Siannodel', 'Xiloscient']

	#----------------------------------------------------------------#

	halfling_firstnames = []
	halfling_lastnames = []
	
	#----------------------------------------------------------------#

	dwarf_firstnames = ['Adrik', 'Alberich', 'Baern', 'Barendd', 'Buren', 'Dain', 'Delg', 'Einkil', 'Eistin',
	'Rangran', 'Thorik', 'Urrek', 'Vein',]
	dwarf_lastnames = ['Battlehammer', 'Stoutbrew', 'Amberbeard', 'Stormbraid', 'Gemforge', 'Rockroller', 'Thunderkiln', 'Flameaxe',]

	#----------------------------------------------------------------#

	halforc_firstnames = []
	halforc_lastnames = []

	#----------------------------------------------------------------#

	halfelf_firstnames = []
	halfelf_lastnames = []

	#----------------------------------------------------------------#

	tiefling_firstnames = []
	tiefling_lastnames = []

	#----------------------------------------------------------------#

	def __init__(self, rFlag):
		'''
		TODO: more initializing
		with the below section, keep in mind will work only if another part
		of the code somewhere else randomly decides which flag from a list
		will be chosen. Worth fiddling around with later.
		'''
		self.rFlag = rFlag
		return


	def getName(self):
		# TODO: code here, depending on the correct race type
		if self.rFlag == 'G':
			first = self.generic_firstnames[randint(0, len(self.generic_firstnames) - 1)]
			last = self.generic_lastnames[randint(0, len(self.generic_lastnames) - 1)]
			return first, last
		''' 
			the rFlag works, the first/last tuple for names works. 
			TODO: look for a more graceful way of handling this outside of a bunch of if's 
		'''
		if self.rFlag == 'Hu':
			first = self.generic_firstnames[randint(0, len(self.human_firstnames) - 1)]
			last = self.generic_lastnames[randint(0, len(self.human_lastnames) - 1)]
			return first, last
			
		if self.rFlag == 'EL':
			first = self.generic_firstnames[randint(0, len(self.elf_firstnames) - 1)]
			last = self.generic_lastnames[randint(0, len(self.elf_lastnames) - 1)]
			return first, last
			
		if self.rFlag == 'HL':
			first = self.generic_firstnames[randint(0, len(self.halfling_firstnames) - 1)]
			last = self.generic_lastnames[randint(0, len(self.halfling_lastnames) - 1)]
			return first, last
			
		if self.rFlag == 'DW':
			first = self.generic_firstnames[randint(0, len(self.dwarf_firstnames) - 1)]
			last = self.generic_lastnames[randint(0, len(self.dwarf_lastnames) - 1)]
			return first, last
			
		if self.rFlag == 'HO':
			first = self.generic_firstnames[randint(0, len(self.halforc_firstnames) - 1)]
			last = self.generic_lastnames[randint(0, len(self.halforc_lastnames) - 1)]
			return first, last
			
		if self.rFlag == 'HE':
			first = self.generic_firstnames[randint(0, len(self.halfelf_firstnames) - 1)]
			last = self.generic_lastnames[randint(0, len(self.halfelf_lastnames) - 1)]
			return first, last
			
		if self.rFlag == 'TL':
			first = self.generic_firstnames[randint(0, len(self.tiefling_firstnames) - 1)]
			last = self.generic_lastnames[randint(0, len(self.tiefling_lastnames) - 1)]
			return first, last
	

	def setFlag(self, rFlag):
		# purely to update the flag, mostly for testing, but we'll see?
		self.rFlag = rFlag



# end class

''' Test Case Block, blocking them out once confirmed to work. '''
ng = NameGenerator('G')
i = 0

while i < 10:
	print(ng.getName())
	i += 1
