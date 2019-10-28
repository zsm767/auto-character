from random import *

class CharacterRace:

	rFlags = ['HU', 'EL', 'HL', 'DW', 'HO', 'HE', 'TL',]
	rFlag = ''
	stats = {'STR': 0, 'DEX': 0, 'CON': 0, 'INT': 0, 'WIS': 0, 'CHA': 0,}

	''' TO-DO: more of the code here '''

	def setRandRace():
		self.rFlag = self.rFlags[randint(0, len(self.rFlags) - 1)]
		return self.rFlag


	def __init__(self):
		# TO-DO (you know the drill)
		setRandRace()

	def setHuStatBonus():
		# TO-DO: update 'stats' dict based off of default bonuses


	def setElStatBonus():
		# TO-DO: update 'stats' dict based off of default bonuses


	def setHLStatBonus():
		# TO-DO: update 'stats' dict based off of default bonuses


	def setDwStatBonus():
		# TO-DO: update 'stats' dict based off of default bonuses


	def setHoStatBonus():
		# TO-DO: update 'stats' dict based off of default bonuses


	def setHeStatBonus():
		# TO-DO: update 'stats' dict based off of default bonuses


	def setTlStatBonus():
		# TO-DO: update 'stats' dict based off of default bonuses


#end CharRace