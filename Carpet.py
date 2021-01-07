def solution(brown, yellow):
    area = brown + yellow
    for i in range(3, area // 3 + 1):
        if area % i != 0:
            continue
        print((i * 2) + (yellow / (i - 2)) * 2, i, i*2, yellow/(i-2)*2)
        if (i * 2) + (yellow / (i - 2) * 2) == area:
            return [i, area // i]


brown = 10
yellow = 2
print(solution(brown, yellow))