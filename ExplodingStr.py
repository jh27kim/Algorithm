import sys

string = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
stack = ""

for c in string:
    stack += c
    if len(stack) >= len(bomb) and stack[-len(bomb):] == bomb:
        print(stack[-len(bomb):])
        print(stack[:-len(bomb)])
        stack = stack[:-len(bomb)]

if stack == "":
    print('FURLA')
else:
    print(stack)
