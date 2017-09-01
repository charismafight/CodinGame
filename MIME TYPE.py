from collections import defaultdict

n, q = int(input()), int(input())  # Number of elements which make up the association table.
MIME = defaultdict(lambda: 'UNKNOWN')
for x in range(n):
    r, h = input().split()
    MIME[r.lower()] = h
for i in range(q):
    fname = input()  # One file name per line.
    inx = fname.rfind('.')
    print('UNKNOWN') if inx == -1 else print(MIME[fname[fname.rfind('.') + 1:].lower()])
