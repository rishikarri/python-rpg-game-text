# let's create a character class that has self health, pwer 

class Character(object):
	def __init__(self, name, health, power):
		self.health = health
		self.power = power 
		self.name = name 

	# this method has access to self because it is a character
	def say_hi(self):
		print "Hello, my name is %s" % (self.name)


# now let's try making an actual character and passing it the correct parameters 

# In this case Rishi is self 
# Rishi = Character("Rishi", 10, 12)
# Patson = Character("Patson", 10, 15)

# Patson.say_hi() 


# print vars(Rishi)



		
