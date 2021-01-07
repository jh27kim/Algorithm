T = int(input())
result = []

for i in range(T):
    N = int(input())
    fives = 5
    answer = 0
    while N >= fives:
        answer += N // fives
        fives = fives * 5
    result.append(answer)

print(*result, sep="\n")
