#!/usr/bin/python3
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number == 0:
    LastD = 0
elif number > 0:
    LastD = number % 10
else:
