from random import *

class NameGenerator:
	rFlag = 'G'
	
	generic_firstnames = ['Greg','Samuel','Mark','Tom','Timothy',
						  'Harold','John','Todd','Ken','Craig',] # TODO: some default names, more can come later
	generic_lastnames = ['Johnson','Wordsworth','Frank','Doe','Smith'
						,'Appleton','Smallpox','Wilson','Long','Short',] # TODO: same as above...

	# specific dicts (maybe can just use lists, since accessing times aren't an issue...
	# for races
	#----------------------------------------------------------------#

	human_firstnames = []
	human_lastnames = []

	#----------------------------------------------------------------#

	elf_firstnames = []
	elf_lastnames = []

	#----------------------------------------------------------------#

	halfling_firstnames = []
	halfling_lastnames = []
	
	#----------------------------------------------------------------#

	dwarf_firstnames = []
	dwarf_lastnames = []

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
		# TODO: more initializing
		# with the below section, keep in mind will work only if another part
		# of the code somewhere else randomly decides which flag from a list
		# will be chosen. Worth fiddling around with later.
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
			TODO: implement the other name lists
		'''
		if self.


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
