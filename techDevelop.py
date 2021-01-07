import copy


def solution(progresses, speeds):
    answer = []
    queue = copy.deepcopy(list(reversed(progresses)))
    speeds = list(reversed(speeds))
    while queue:
        if queue[-1] >= 100:
            cnt = 0
            while True:
                if queue[-1] >= 100:
                    queue.pop()
                    speeds.pop()
                    cnt += 1
                    if not queue:
                        break
                else:
                    break
            answer.append(cnt)
        queue = [sum(x) for x in zip(queue, speeds)]
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))
