# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    list = [int(input()) for i in range(8)]
    print([x for x, y in enumerate(list) if max(list) == y][0])
