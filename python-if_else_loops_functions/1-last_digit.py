#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lasd = abs(number) % 10
if number < 0:
	lasd = -lasd
print("Last digit of {} is {} and is".format(number, lasd), end=" ")
if lasd > 5:
	print("greater than 5")
elif lasd == 0:
	print("0")
else:
	print("less than 6 and not 0")
