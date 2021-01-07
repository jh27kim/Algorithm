import sys

location = sys.stdin.readline()
movement = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
x, y = int(location[1])-1, ord(location[0])-97
print(x, y)
answer = 0

for m in movement:
    nx, ny = x + m[0], y + m[1]
    if 0 <= nx < 8 and 0 <= ny < 8:
        answer += 1
print(answer)