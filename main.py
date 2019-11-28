#!/usr/bin/python3

from PIL import Image
import numpy as np
import image_helpers
import sys

def print_usage():
    """
        Print out what parameters can be passed into the main.py
    """

    print("\nUSAGE:\n")

    commands = {"-f"  :   "image path",
                "-rw" :   "resize width",
                "-rh" :   "resize height",
                "-u"  :   "total available units",
                "-uf" :   "path for available units file"}

    for i in commands:

        print("    " + i + ":", commands[i])

    print("")

def illegal_inputs(inputs):
    """
        Modify this to check whether inputs given to main.py are valid or not
    """

    return False

if __name__ == "__main__":

    inputs = sys.argv[1:]

    if inputs == ['-h'] or inputs == [] or illegal_inputs(inputs):

        print_usage()
