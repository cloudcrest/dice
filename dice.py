

from specialInput import *

numDice = int_input("Hi. How many dice would you like to roll? ")

import random

for x in range(numDice):
    numSides = int_input("OK. Now tell me, this fabulous program who is doing you this great favor, how many sides you'd like on your die. ")
    print random.randint(1, numSides)

