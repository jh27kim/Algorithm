T = input()
P = input()
table = [0 for _ in range(len(P))]

j = 0
for i in range(1, len(P)):
    while j > 0 and P[i] != P[j]:
        j = table[j-1]
    if P[i] == P[j]:
        j += 1
        table[i] = j

j = 0
ans = 0
loc = []
for i in range(len(T)):
    while j > 0 and T[i] != P[j]:
        j = table[j-1]
    if T[i] == P[j]:
        if j == len(P) - 1:
            loc.append(i-j+1)
            j = table[j]
            ans += 1
        else:
            j += 1

print(ans)
print(*loc)