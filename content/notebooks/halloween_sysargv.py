"""
This is a spooky demonstration of using sys.argv to provide a python script with inputs.
"""
import sys

# access inputs with sys.argv and save them in a list:
inputs = sys.argv[1:]
# all elements of sys.argv are strings, but we want these inputs to be of different types:
number = int(inputs[0])
lantern = inputs[1]
animals = inputs[2].split(',')
# check the types of the variables now
print("{} is a {}".format(number, type(number)))
print("{} is a {}".format(lantern, type(lantern)))
print("{} is a {}".format(animals, type(animals)))
# get the name of the program
print("This program is called {}".format(sys.argv[0]))
