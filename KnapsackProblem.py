from bisect import bisect_right

N, C = map(int, input().split())
weights = list(map(int, input().split()))
cnt = 0

a_weight = weights[:N//2]
b_weight = weights[N//2:]


def a_brute_force(l, w):
    print(l, w)
    if l >= len(a_weight):
        a_sum.append(w)
        return
    a_brute_force(l + 1, w)
    a_brute_force(l + 1, w + a_weight[l])


def b_brute_force(l, w):
    if l >= len(b_weight):
        b_sum.append(w)
        return
    b_brute_force(l + 1, w)
    b_brute_force(l + 1, w + b_weight[l])


a_sum = []
b_sum = []
a_brute_force(0, 0)
b_brute_force(0, 0)
b_sum.sort()

for i in a_sum:
    if C - i < 0:
        continue
    cnt += (bisect_right(b_sum, C-i)+1)

print(cnt)
