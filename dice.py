#! /usr/bin/env python

from specialInput import *

numSides = int_input("Hi. How many sides would you like your dice to have? ")


while numSides <= 2:
    print "Sorry, but that's impossible. Try again."
    numSides = int_input("Hi. How many sides would you like your dice to have? ")

numDice = int_input("OK. How many dice would you like to roll? ")

import random

for x in range(0, numDice):
    print random.randint(1, numSides)


