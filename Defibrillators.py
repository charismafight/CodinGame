import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def e_float(s):
    return float(s.replace(',', '.'))


def distance(*args):
    x = (e_float(args[4]) - e_float(lon)) * math.cos((e_float(lat) + e_float(args[5])) / 2)
    y = e_float(args[5]) - e_float(lat)
    return math.sqrt(x ** 2 + y ** 2) * 6371, args[1]


lon = input()
lat = input()
n = int(input())
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
# Requirements:
# The input data you require for your program is provided in text format.
# This data is comprised of lines, each of which represents a defibrillator.
# Each defibrillator is represented by the following fields:
# A number identifying the defibrillator
# Name
# Address
# Contact Phone number
# Longitude (degrees)
# Latitude (degrees)
# These fields are separated by a semicolon (;).
#
# Beware: the decimal numbers use the comma (,) as decimal separator.
#  Remember to turn the comma (,) into dot (.) if necessary in order to use the data in your program.

# calculate distance between a single defibrillator to user
print(sorted([distance(*input().split(';')) for x in range(n)])[0][1])
