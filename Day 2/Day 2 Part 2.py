# create empty lists
inputs = []
possgames = []

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
        # reset maximum cubes to 0
        maxred = 0
        maxgreen = 0
        maxblue = 0
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
                if colour == 'red' and amount > maxred: maxred = amount
                elif colour == 'green' and amount > maxgreen: maxgreen = amount
                elif colour == 'blue' and amount > maxblue: maxblue = amount
        # append power of minimum cubes to possgames
        possgames.append(maxred * maxgreen * maxblue)


# sum all possible game numbers
total = sum(possgames)
print(total)