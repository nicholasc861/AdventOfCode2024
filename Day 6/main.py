import os

# Standard boilerplate to read input file
dirname = os.path.dirname(__file__)
input_file = os.path.join(dirname, 'input')

# Read as string
f = open(input_file, "r").read()

if __name__ == "__main__":
    groups = f.split("\n")
    starting_pos = (0, 0)

    # Retrieve starting position of guard as (x, y) coordinate
    for idx, group in enumerate(groups):
        if ("^" in group):
            starting_pos = (idx, group.index("^"))


    print(starting_pos)