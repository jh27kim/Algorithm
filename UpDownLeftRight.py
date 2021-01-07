import sys

N = int(sys.stdin.readline())
movement = sys.stdin.readline().split()
x, y = 0, 0


for m in movement:
    if m == 'R':
        if y+1 < N:
            y += 1
    elif m == "L":
        if y-1 >= 0:
            y -= 1
    elif m == "U":
        if x-1 >= 0:
            x -= 1
    elif m == "D":
        if x + 1 < N:
            x += 1
print(x+1, y+1)

