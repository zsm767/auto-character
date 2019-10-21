import random

class DiceRoller:

  def __init__():
    #blank init statement?


  def 1d4():
    return randint(1, 4)


  def 1d6():
    return randint(1, 6)


  def 1d8():
    return randint(1, 8)


  def 1d12():
    return randint(1, 12)


  def 1d20():
    return randint(1, 20)


#end DiceRoller


#NOTE: This can be commented out / removed later after confirmation of success. 
#some small tests:
dr = DiceRoller()

#testing each die individually, doing 10 rolls of each

print('\nTesting 4-sided die')
i = 0
while i < 10:
  print(dr.1d4())
  i += 1

print('\nTesting 6-sided die')
i = 0
while i < 10:
  print(dr.1d6())
  i += 1

print('\nTesting 8-sided die')
i = 0
while i < 10:
  print(dr.1d8())
  i += 1

print('\nTesting 12-sided die')
i = 0
while i < 10:
  print(dr.1d12())
  i += 1

print('\nTesting 20-sided die')
i = 0
while i < 10:
  print(dr.1d20())
  i += 1