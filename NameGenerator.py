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

	human_firstnames = ['Gauwilh', 'Eglod', 'Gerey', 'Hilda', 'Adin', 'Rere', 'Eleth ', 'Helman', 'Atell', 'Freyny',]
	human_lastnames = ['Velley', 'Shile', 'Gysby', 'Vissio', 'Falconsflight', 'Carter', 'Trannyth', 'Shieldheart', ]

	#----------------------------------------------------------------#

	elf_firstnames = ['Aust', 'Adra', 'Berrian', 'Birel', 'Carric', 'Caelynn', 'Erevan', 'Felosial', 'Ivellion', 'Quarion', 'Lia',
	'Varis', 'Xanathi',]
	elf_lastnames = ['Amakiir', 'Amastacia', 'Galanodel', 'Holion', 'Liadon', 'Meliamne', 'Siannodel', 'Xiloscient',]

	#----------------------------------------------------------------#

	halfling_firstnames = ['Symund', 'Hileon', 'Artis', 'Herim', 'Richye', 'Suse', 'Phily', 'Peona', 'Rosa', 'Gela', 'Mara',]
	halfling_lastnames = ['Folcey', 'Burrow', 'Ophirn', 'Mere', 'Mere', 'Wellsor',]
	
	#----------------------------------------------------------------#

	dwarf_firstnames = ['Adrik', 'Alberich', 'Baern', 'Barendd', 'Buren', 'Dain', 'Delg', 'Einkil', 'Eistin',
	'Rangran', 'Thorik', 'Urrek', 'Vein',]
	dwarf_lastnames = ['Battlehammer', 'Stoutbrew', 'Amberbeard', 'Stormbraid', 'Gemforge', 'Rockroller', 'Thunderkiln', 'Flameaxe',]

	#----------------------------------------------------------------#

	halforc_firstnames = ['Elgold', 'Davkul', 'Wilros', 'Uaerris', 'Quiora', 'Seahand', 'Magkain', 'Quikain', 'Sadasaadi', 'Olofalcon',]
	halforc_lastnames = ['Fiedlerson', 'Wyvernjack', 'Windsailor', 'Pegason', 'Arroway', 'Trannyth', 'Waveharp',]

	#----------------------------------------------------------------#

	halfelf_firstnames = ['Coratis', 'Horven', 'Gurstina', 'Stoora', 'Arathana', 'Arahana', 'Ianmorn', 'Yenrry', 'Belben', ]
	halfelf_lastnames = ['Wolfsbane', 'Joysword', 'Dawntracker', 'Gentleharp', 'Shipsail', 'Darkeyes', 'Chorster', 'Hollysword',]

	#----------------------------------------------------------------#

	tiefling_firstnames = ['Azza', 'Ea', 'Ishte', 'Aym', 'Manea', 'Markosian', 'Ahrim', 'Iados', 'Andram', 'Amnon', 'Xappan', 'Zephan',]
	tiefling_lastnames = ['Remorse', 'Belief', 'Aid', 'Talent', 'Fealty', 'Revulsion', 'Violence', 'Scorn', 'Creed', 'Power', 'Haste',]

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
		if self.rFlag == 'HU':
			first = self.human_firstnames[randint(0, len(self.human_firstnames) - 1)]
			last = self.human_lastnames[randint(0, len(self.human_lastnames) - 1)]
			return first, last
			
		if self.rFlag == 'EL':
			first = self.elf_firstnames[randint(0, len(self.elf_firstnames) - 1)]
			last = self.elf_lastnames[randint(0, len(self.elf_lastnames) - 1)]
			return first, last
			
		if self.rFlag == 'HL':
			first = self.halfling_firstnames[randint(0, len(self.halfling_firstnames) - 1)]
			last = self.halfling_lastnames[randint(0, len(self.halfling_lastnames) - 1)]
			return first, last
			
		if self.rFlag == 'DW':
			first = self.dwarf_firstnames[randint(0, len(self.dwarf_firstnames) - 1)]
			last = self.dwarf_lastnames[randint(0, len(self.dwarf_lastnames) - 1)]
			return first, last
			
		if self.rFlag == 'HO':
			first = self.halforc_firstnames[randint(0, len(self.halforc_firstnames) - 1)]
			last = self.halforc_lastnames[randint(0, len(self.halforc_lastnames) - 1)]
			return first, last
			
		if self.rFlag == 'HE':
			first = self.halfelf_firstnames[randint(0, len(self.halfelf_firstnames) - 1)]
			last = self.halfelf_lastnames[randint(0, len(self.halfelf_lastnames) - 1)]
			return first, last
			
		if self.rFlag == 'TL':
			first = self.tiefling_firstnames[randint(0, len(self.tiefling_firstnames) - 1)]
			last = self.tiefling_lastnames[randint(0, len(self.tiefling_lastnames) - 1)]
			return first, last
	

	def setFlag(self, rFlag):
		# note: rFlag global var is set to 'G' by default (if non-param init is called)
		self.rFlag = rFlag



# end class

''' 
Test Case Block, blocking them out once confirmed to work. 

ng = NameGenerator('HU')
ng2 = NameGenerator('EL')
ng3 = NameGenerator('HL')
ng4 = NameGenerator('DW')
ng5 = NameGenerator('HO')
ng6 = NameGenerator('HE')
ng7 = NameGenerator('TL')

i = 0

while i < 10:
	print(ng.getName())
	print(ng2.getName())
	print(ng3.getName())
	print(ng4.getName())
	print(ng5.getName())
	print(ng6.getName())
	print(ng7.getName())
	i += 1
```