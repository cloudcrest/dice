#! /usr/bin/env python

from specialInput import *

numDice = int_input("How many dice would you like to roll? ")

import random

for x in range(numDice):
    while numSides <= 2:
        print "Sorry, but that's impossible. Try again."
        numSides = int_input("Hi. How many sides would you like your dice to have? ")
    print random.randint(1, numSides)


