from monsters import Goblin
from hero import Hero

# let's make two characters that will fight each other 
Rishi = Hero("Rishi", 10, 12, 'bow')
evil_goblin = Goblin("evil goblin", 9, 3)

# Run greeting 


print ("You have encountered an %s!") % evil_goblin.name

while Rishi.is_alive():
	print "What will you do? "
	print "1. Fight %s" % evil_goblin.name
	print "2. Run away %s" % evil_goblin.name
	print "> ",

	input = int(raw_input())

	if input == 1:
		print 'you fight'
		break
	if input == 2:
		print 'you run'
		break



# print Rishi.is_alive()

# now we can actually run logic to get them to fight

