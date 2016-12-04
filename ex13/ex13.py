#from sys import argv

#script, first, second, third = argv

#print "The script is called:", script
#print "Your first variable is:", first
#print "You second variable is:", second
#print "Your third variable is:", third

#from sys import argv

#running, away_from = argv

#print "You are running: ", running
#print "To get away from: ", away_from

from sys import argv

script, first, second, third, fourth = argv

name = raw_input("What is your name? ")

print "Your name is %r" % (name)

print "The best script ever:", script
print "It's fun to stay at the:", first
print "And eat:", second
print "With a:", third
print "Follow by:", fourth