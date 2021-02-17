t = int(input())
case = [list(map(int, input().split())) for _ in range(t)]
prize_a = [5000000, 3000000, 2000000, 500000, 300000, 100000]
prize_b = [5120000, 2560000, 1280000, 640000, 320000]

for a, b in case:
    start_a, start_b = 1, 1
    rank_a, rank_b = 0, 0
    res = 0
    while a > 0:
        a -= start_a
        start_a += 1
        rank_a += 1
    while b > 0:
        b -= start_b
        start_b *= 2
        rank_b += 1
    if 0 < rank_a <= 6:
        res += prize_a[rank_a-1]
    if 0 < rank_b <= 5:
        res += prize_b[rank_b-1]
    print(res)



