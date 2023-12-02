# create empty lists
inputs = []
first_digits = []
second_digits = []
all_nums = []

# create list of all numbers we are looking for
nums = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'orez',
    'eno',
    'owt',
    'eerht',
    'ruof',
    'evif',
    'xis',
    'neves',
    'thgie',
    'enin'
]

# create dictionary to map all nums to ints
num_dict = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'orez': 0,
    'eno': 1,
    'owt': 2,
    'eerht': 3,
    'ruof': 4,
    'evif': 5,
    'xis': 6,
    'neves': 7,
    'thgie': 8,
    'enin': 9
}

# initialize variables
notfound= True
count = 0

# Read in input file, strip newline character, append to inputs list
with open('input.txt') as file:
    for line in file:
        # strip off newline
        code = line.rstrip('\n')
        inputs.append(code)

# extract digit
# loop through each item in file
for item in inputs[:]:
    # set required variable to be blank
    string = ''
    first_element = []
    second_element = []
    # loop through characters in item string one at a time
    for char in item:
        # append each character to a string
        string = string + char
        # find if any of the elements in nums list are in the string
        first_element = [element for element in nums if element in string]
        # if an element is found, use the dictionary to create the correct integer
        if first_element != []:
            first_element = num_dict[first_element[0]]
            #print('first digit: ' + str(first_element))
            first_digits.append(first_element)
            break
    # repeat for reversed string (i.e. search from the end character backwards)
    string = ''
    for char in reversed(item):
        string = string + char
        second_element = [element for element in nums if element in string]
        if second_element != []:
            second_element = num_dict[second_element[0]]
            #print('second digit: ' + str(second_element))
            second_digits.append(second_element)
            break

all_nums = zip(first_digits, second_digits)
total = []
for item1, item2 in all_nums:
    total.append(int(str(item1) + str(item2)))
print(sum(total))


#total = sum(alldigits)
#print(total)
