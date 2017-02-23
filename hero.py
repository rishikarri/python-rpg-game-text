from character import Character
from monsters import evil_goblin

class Hero(Character): 

	# this first initialization consists of the parameters that every Hero will get 
	def __init__(self, name, health, power, weapon):
		Character.__init__(self, name, health, power)
		self.weapon = weapon
		# self.name = name
		# self.health = health
		# self.power = power
	
	def attack(self, what_to_attack):
		print ("%s has attacked %s and has dealt %d damage") % (self.name, what_to_attack.name, self.power)

	# now we are going to give the hero access to the Character methods - in order to do so, we need to pass up the props we just received
		
		




# Rishi.say_hi()

# Rishi.attack(evil_goblin)
# print Rishi.weapon
