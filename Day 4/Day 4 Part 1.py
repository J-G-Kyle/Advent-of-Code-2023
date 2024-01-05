inputs = []

with open('allcards.txt') as file:
    for line in file:
        # strip off newline
        code = line.rstrip('\n')
        inputs.append(code)

total = 0
addition = 0

for card in inputs:
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
    # numbers you have, four of them (48, 83, 17, and 86) are winning numbers!
    # That means card 1 is worth 8 points (1 for the first match, then
    # doubled three times for each of the three matches after the first).
    # 1 * 2 * 2 * 2
    # 1 * (2 * n - 1)
    n = len(matches)
    if n > 0:
        addition = (2**(n-1))
    else:
        addition = 0
    print(addition)
    total += addition

print(total)