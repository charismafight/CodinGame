import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
if n == 0:
    print(0)
temps = list(map(int, input().split()))
temps.sort(reverse=True)
print([x for x in temps if math.fabs(x) == min([int(math.fabs(y)) for y in temps])][0])
