import sys

string = sys.stdin.readline().rstrip()
alphabets = []
number = 0

for s in string:
    if s.isalpha():
        alphabets.append(s)
        continue
    print(s)
    number += int(s)

alphabets.sort()
answer = "".join(alphabets) + str(number)
print(answer)
