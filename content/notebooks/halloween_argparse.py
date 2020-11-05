"""
This is a spooky demonstration of using argparse to provide a python script with inputs.
"""
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-n", "--number",
                    action="store", type=float,
                    help="An unlucky number (float).")
parser.add_argument("-l", "--lantern",
                    action="store", type=str, default="pumpkin",
                    help="Material to carve a lantern out of (string, default is pumpkin).")
parser.add_argument("-a", "--animals",
                    action="store", type=str, default='',
                    help=("A comma separated list of animals typically associated with halloween. "
                          "Example: bat,cat,rat (string)"))
parser.add_argument("-c", "--christmas",
                    action="store_true", default=False,
                    help="Indicate whether it is Christmas yet (bool, default is False).")
args = parser.parse_args()

# split the comma separated values in the animals argument
animals = args.animals.split(',')

# check the types of the variables:
print("{} is a {}".format(args.number, type(args.number)))
print("{} is a {}".format(args.lantern, type(args.lantern)))
print("{} is a {}, but {} is a {}".format(args.animals, type(args.animals), animals, type(animals)))
print("{} is a {}".format(args.christmas, type(args.christmas)))
