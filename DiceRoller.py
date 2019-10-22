from random import *

class DiceRoller:

	def __init__(self):
		#blank init statement?
		return
		
	def d4(self):
		return randint(1, 4)


	def d6(self):
		return randint(1, 6)


	def d8(self):
		return randint(1, 8)


	def d12(self):
		return randint(1, 12)


	def d20(self):
		return randint(1, 20)


#end DiceRoller


#NOTE: This can be commented out / removed later after confirmation of success. 
#some small tests:
dr = DiceRoller()

#testing each die individually, doing 10 rolls of each

print('\nTesting 4-sided die')
i = 0
while i < 10:
  print(dr.d4())
  i += 1

print('\nTesting 6-sided die')
i = 0
while i < 10:
  print(dr.d6())
  i += 1

print('\nTesting 8-sided die')
i = 0
while i < 10:
  print(dr.d8())
  i += 1

print('\nTesting 12-sided die')
i = 0
while i < 10:
  print(dr.d12())
  i += 1

print('\nTesting 20-sided die')
i = 0
while i < 10:
  print(dr.d20())
  i += 1