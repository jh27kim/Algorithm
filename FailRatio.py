def solution(N, stages):
    answer = []
    players = len(stages)

    challengers = [0] * (N+1)

    for s in stages:
        challengers[s-1] += 1

    for i in range(N):
        #print(answer)
        if players == 0:
            answer.append([0, i])
            continue

        answer.append([challengers[i]/players, i])
        players -= challengers[i]

    answer.sort(key=lambda x:(-x[0], x[1]))

    return [i[1]+1 for i in answer]


N = 4
stages = [2,2,2,2,2]
print(solution(N, stages))