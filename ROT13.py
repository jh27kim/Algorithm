import string

S = input()
answer = []
ind = 0

LowerCases = dict(zip(list(string.ascii_lowercase), range(1, 27)))
UpperCases = dict(zip(list(string.ascii_uppercase), range(1, 27)))
LowKeys = list(LowerCases.keys())
UpKeys = list(UpperCases.keys())

for i in S:
    if i.isspace() or i.isdigit():
        answer.append(i)
        continue
    if i.isupper():
        ind = UpperCases[i] + 13
        if ind > 26:
            ind = ind % 26
        answer.append(UpKeys[ind-1])

    else:
        ind = LowerCases[i] + 13
        if ind > 26:
            ind = ind % 26
        answer.append(LowKeys[ind-1])

print("".join(answer))