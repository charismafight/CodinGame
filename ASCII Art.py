import sys
import math
import string

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

lines = []
for i in range(h):
    # this input contains all 27 characters we need
    # so substring it should be a good way
    row = input()
    lines.append(row)


# every 4 columns has a letter so we should find a mapping to num and character then fix the caps
def get_index():
    index = []
    for letter in t.lower():
        if letter not in string.ascii_lowercase:
            index.append(26)
        else:
            index.append(string.ascii_lowercase.find(letter.lower()))
    return index


idx = get_index()
for i in range(h):
    for j in idx:
        print(lines[i][l * j:l * (j + 1)], end='')
    print("")
