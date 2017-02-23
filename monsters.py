# go to the character.py file and grab the Character class cause we will have to use that ****

from character import Character

# create an instance of a monster 

# in theory this should automatically have health power and say hi method
class Goblin(Character):
	def __init__(self, name, health, power):
		Character.__init__(self, name, health, power)

	def goblin_say_hi(self):
		print "he he he - I am an evil goblin and my name is %s" % (self.name)
		# self.name = "goblin"
		# self.health = 9
		# self.power = 3

# now this goblin has all of the properties of a character

evil_goblin = Goblin("goblin0", 9, 3)

# evil_goblin.say_hi()
# evil_goblin.goblin_say_hi()

# now the goblin has access goblin functions and all character functions 