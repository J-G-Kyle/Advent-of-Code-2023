from collections import Counter
import re

# create empty items
input = []
symbols = []
c = Counter()

# read input into a 2D array
file = open('Test1.txt')
# put lines into a 2D array
for line in file:
    # strip newline character
    line = line.rstrip('\n')
    # cast line into a list
    line = list(line)
    # append into a list of lists
    input.append(line)
    # update counts
    c.update(line)
    # set max length of line (total columns)
    if len(line) > maxcol: maxcol = len(line)
    # check for all the symbols

# set regex pattern for numeric and "." only
pattern = re.compile("[0-9.]")

# try to get only the symbols from the input
for k, v in c.items():
    if not re.match(pattern, k):
        print(k + ": " + str(v))
        symbols.append(k)

# create empty list of tuples
tuples = []
# input[row number - j][column number - i]
for j in range(len(input)):
    for i in range(maxcol):
        # if character is a symbol generate a tuple of it's position
        if not re.match(pattern, input[j][i]):
            tup = (j, i)
            tuples.append(tup)

# tuples is a list of locations (row, column) of all symbols in input
print(tuples)
def checknum(tuple):
    # regex pattern to match numerals
    numpattern = re.compile("[0-9]")
    # check top left location (-1, -1)
    if tuple[0] > 0 and tuple[1] > 0:
        print(input[tuple[0]][tuple[1]])

checknum((1,3))

