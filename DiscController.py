import heapq


def solution(jobs):
    count, last, answer = 0, -1, 0
    heap = []
    jobs.sort()

    time = jobs[0][0]
    while count < len(jobs):
        for s, t in jobs:
            if last < s <= time:
                heapq.heappush(heap, (t, s))
        if len(heap) > 0:
            count += 1
            last = time
            term, start = heapq.heappop(heap)
            time += term
            answer += time-start
    return answer // len(jobs)


jobs = [[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]
print(solution(jobs))

# 3 10
# 7 10