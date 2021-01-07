import itertools
heights = []


def solution():
    while True:
        for k in range(9, 1, -1):
            comb = list(itertools.combinations(heights, k))
            for j in comb:
                if sum(j) == 100 and len(j) == 7:
                    result = list(j)
                    result.sort()
                    print(*result, sep="\n")
                    return


for i in range(9):
    heights.append(int(input()))
solution()


