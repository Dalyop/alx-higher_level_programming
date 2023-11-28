#!/usr/bin/python3
import random
number = random.randint(-10, 10)
#MY CODE
if number == 0:
    print(f"{number} is zero")
elif number > 0:
    print(f"{number} ia positive")
else:
    print(f"{number} ia negative")
