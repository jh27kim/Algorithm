import itertools

N = int(input())
numbers = list(map(int, input().split()))
operator_count = list(map(int, input().split()))
operators = []

idx = 0
for op in operator_count:
    for i in range(op):
        operators.append(idx)
    idx += 1

operators_combination = set(itertools.permutations(operators, len(operators)))
answer_max = -int(1e9)
answer_min = int(1e9)

for comb in operators_combination:
    res = numbers[0]
    for i in range(1, len(numbers)):
        if comb[i-1] == 0:
            res += numbers[i]
        elif comb[i-1] == 1:
            res -= numbers[i]
        elif comb[i-1] == 2:
            res *= numbers[i]
        elif comb[i-1] == 3:
            if res < 0:
                res = -(abs(res) // numbers[i])
            else:
                res = res // numbers[i]
    #print(comb, res)
    answer_max = max(answer_max, res)
    answer_min = min(answer_min, res)

print(answer_max)
print(answer_min)
