import sys
import binascii

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
# The input message consists of ASCII characters (7-bit)
# The encoded output message consists of blocks of 0
# A block is separated from another block by a space
# Two consecutive blocks are used to produce a series of same value bits (only 1 or 0 values):
# - First block: it is always 0 or 00. If it is 0, then the series contains 1, if not, it contains 0
# - Second block: the number of 0 in this block is the number of bits in the series
def cvt(b_str):
    result = ''
    symbol = ''
    for s in b_str:
        # part one
        if symbol != s:
            # record current value before continue loop
            result += ('' if symbol == '' else ' ') + zero_cvt(s) + ' 0'
            symbol = s
        else:
            # part two
            result += '0'

    return result


def zero_cvt(s):
    return '0' if s == '1'else '00'


# Second example, we want to encode the message CC (i.e. the 14 bits 10000111000011) :
# if char > 1 then combine the strings together
bin_str = ''.join([bin(ord(s)).replace('0b', '').zfill(7) for s in message])
print(cvt(bin_str))
