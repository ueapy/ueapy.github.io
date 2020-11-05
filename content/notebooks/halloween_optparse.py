"""
This is a spooky demonstration of using optparse to provide a python script with inputs.
Note that optparse has been deprecated and is not being developed further. It is replaced with argparse since 3.2.
"""
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-n", "--number",
                  action="store", type="float", dest="number",
                  help="An unlucky number (float).")
parser.add_option("-l", "--lantern",
                  action="store", type="string", dest="lantern", default="pumpkin",
                  help="Material to carve a lantern out of (string, default is pumpkin).")
parser.add_option("-a", "--animals",
                  action="store", type="string", dest="animals", default='',
                  help=("A comma separated list of animals typically associated with halloween. "
                        "Example: bat,cat,rat (string)"))
parser.add_option("-c", "--christmas",
                  action="store_true", dest="christmas", default=False,
                  help="Indicate whether it is Christmas yet (bool, default is False).")
(options, args) = parser.parse_args()

# split the comma separated values in the animals argument
animals = options.animals.split(',')

# check the types of the variables:
print("{} is a {}".format(options.number, type(options.number)))
print("{} is a {}".format(options.lantern, type(options.lantern)))
print("{} is a {}, but {} is a {}".format(options.animals, type(options.animals), animals, type(animals)))
print("{} is a {}".format(options.christmas, type(options.christmas)))
