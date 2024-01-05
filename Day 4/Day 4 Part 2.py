inputs = []

with open('allcards.txt') as file:
    for line in file:
        # strip off newline
        code = line.rstrip('\n')
        inputs.append(code)

# create a dictionary of card number: count of copies
cardcopies = {}
for i in range(len(inputs)):
    cardcopies[i + 1] = 1

def cardnumbers(card):
    numbers = (card.split(":")[1])
    numbers = numbers.split("|")
    # trim off excess spaces at beginning and end, split into
    numbers = [nums.strip().split(" ") for nums in numbers]
    winnums = set(numbers[0])
    if '' in winnums:
        winnums.remove('')
    cardnums = set(numbers[1])
    if '' in cardnums:
        cardnums.remove('')
    # compare sets and generate set of intersections
    matches = winnums.intersection(cardnums)
    # get number of card
    cardnum = str((card.split(":")[0]))
    cardnum = int((cardnum.split()[1]))
    n = len(matches)
    if n > 0:
        # update number of copies in dictionary cardcopies
        for i in range(n):
            cardcopies[cardnum + i + 1] += 1

# update number of copies for each original card
for card in inputs:
    cardnumbers(card)

# update number of copies by interating through each copy of a scratchcard
for key in cardcopies:
    if key > 1:
        for i in range(cardcopies[key] - 1):
            cardnumbers(inputs[key - 1])

print(sum(cardcopies.values()))
