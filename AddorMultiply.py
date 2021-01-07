import sys

s = sys.stdin.readline().rstrip()
answer = max(int(s[0])+int(s[1]), int(s[0])*int(s[1]))

if len(s) <= 2:
    print(answer)
    exit()

for i in range(2, len(s)):
    if int(s[i]) == 0 or int(s[i]) == 1:
        answer += int(s[i])
    else:
        answer *= int(s[i])
print(answer)
