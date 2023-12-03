# create empty lists
inputs = []
possgames = []
# the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
maxred = 12
maxgreen = 13
maxblue = 14

# Read in input file, strip newline character, append to inputs list
with open('inputL.txt') as file:
    for line in file:
        # strip off newline
        line = line.rstrip('\n')
        # seperate out the game number
        gamel = line.split(sep=':')
        gamen = int(gamel[0][5:])
        # subgames
        games = gamel[1].split(sep=';')
        # set possible to True
        possible = True
        # iterate through each game
        for game in games:
            # split each game into sub game of shown dice
            show = game.split(sep=',')
            # loop through each die colour
            for dice in show:
                # strip off excess leading space
                dice = dice.strip()
                # quick and dirty divide into amount and colour around the ' '
                # assumes there will always only be e.g. '3 red' in input
                amount = int(dice.split(sep=' ')[0])
                colour = dice.split(sep=' ')[1]
                # change possible to false if the amount is greater than the max allowed
                if colour == 'red' and amount > maxred: possible = False
                elif colour == 'green' and amount > maxgreen: possible = False
                elif colour == 'blue' and amount > maxblue: possible = False
        # append only possible game numbers to list
        if possible: possgames.append(gamen)

# sum all possible game numbers
total = sum(possgames)
print(total)