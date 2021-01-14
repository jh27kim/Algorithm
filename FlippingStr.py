S = input()
start = S[0]
zeros = 0
ones = 0

if start == '0':
    zeros += 1
else:
    ones += 1

for i in range(1, len(S)):
    if S[i] == start:
        continue
    if S[i] == '1':
        ones += 1
    else:
        zeros += 1
    start = S[i]

print(min(zeros, ones))
