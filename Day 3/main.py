import os

# Standard boilerplate to read input file
dirname = os.path.dirname(__file__)
input_file = os.path.join(dirname, 'input')

# Read as string
f = open(input_file, "r").read()

if __name__ == "__main__":
    