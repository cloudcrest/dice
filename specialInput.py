#No shebang
#this program won't run because it is a module, or just a list of functions and definitions that other programs will use. No main command functions, print statements; no main program here.

def name_input(prompt):
    name = raw_input(prompt)
    if len(name) >= 10:
        print "That name is too long. I'll give you a nickname."
        name = name[0:9]
        print name
    return name


def int_input(prompt):
    while 1 == 1:
        number = raw_input(prompt)
        try:
            number = int(number)
            return number
        except:
            print "That's not a number! Try again!" 

def float_input(prompt):
    #infinite loop, or write while True
    while 1==1:
        number = raw_input(prompt)
        try:
            number = float(number)
            return number
        except:
            print "Those are not numbers! Try again!"
        

