
# ask the user how many dice, then ask how many sides each die has. (ie - 5 sided die and 12 sided die)

# keep numSides
# keep numDice
# put numsides in forloop.


# ------------------------------------------------------------------------------


from specialInput import *

numSides = int_input("Hi. How many sides would you like your dice to have? ")

numDice = int_input("OK. How many dice would you like to roll? ")

import random

for x in range(0, numDice):
    print random.randint(1, numSides)

