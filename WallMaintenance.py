answer = int(1e9)


def solution(n, weak, dist):
    worker = [0 for _ in range(len(dist))]

    queue = []
    dfs(queue, weak, dist, worker)

    return answer


def dfs(queue, weak, dist, worker):
    global answer

    #print(queue)

    if check(queue, weak):
        #print(answer)
        answer = min(answer, len(queue))
        #print(queue, answer)

    for i in range(n):
        for j in range(len(dist)):
            if worker[j]:
                continue

            worker[j] = 1
            queue.append([i, dist[j]])
            dfs(queue, weak, dist, worker)
            queue.pop()
            worker[j] = 0


def check(queue, weak):
    result = []
    for w in weak:
        repaired = False
        for start, d in queue:
            for i in range(start, start + d):
                i = i % n
                if w == i:
                    repaired = True
                    break

            for j in range(start, start-d, -1):
                if j == w:
                    repaired = True
                    break

        if not repaired:
            return False

    return repaired

from itertools import permutations

def solution(n, weak, dist):
    L = len(weak)
    cand = []
    weak_point = weak + [w+n for w in weak]

    for i, start, in enumerate(weak):
        for friends in permutations(dist):
            count = 1
            position = start
            for friend in friends:
                position += friend

                if position < weak_point[i+L-1]:
                    count += 1
                    position = [w for w in weak_point[i+1:i+L] if w > position][0]
                else:
                    cand.append(count)
                    break

    return min(cand) if cand else -1



n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))
#check([[7, 4]], weak)