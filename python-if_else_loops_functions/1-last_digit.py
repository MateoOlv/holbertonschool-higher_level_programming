#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = number % 10

if lastd < 0:
    lastd *= -1
if number == 0:
	lastd = 0  
if lastd > 5:
	status = ("is greater than 5")
elif lastd == 0:
	status = ("is 0")
else:
	status = ("is less than 6 and not 0")
print("Last digit of {0} is {1} and {2}".format(number, lastd, status))
