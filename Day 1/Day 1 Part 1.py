# create empty lists
inputs = []
alldigits = []

# create list of digits
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Read in input file, strip newline character, append to inputs list
with open('input.txt') as file:
    for line in file:
        # strip off newline
        code = line.rstrip('\n')
        inputs.append(code)

# extract digit
for item in inputs:
    # reset list to empty
    itemdigits = []
    # loop through characters in string and if a digit is there, append it to a list.
    for char in item:
        if char in digits:
            itemdigits.append(char)
    # concat first and last digit to a two digit string, cast that to an int and append to a list
    if len(itemdigits) > 0:
        twodigits = itemdigits[0] + itemdigits[-1]
        alldigits.append(int(twodigits))

total = sum(alldigits)
print(total)
