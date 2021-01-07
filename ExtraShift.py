def solution(n, works):
    while n:
        work = works.pop(works.index(max(works)))
        if work == 0:
            return sum(i * i for i in works)
        else:
            works.append(work-1)
            n -= 1
    return sum(i*i for i in works)


works = [1, 1]
n = 3
print(solution(n, works))