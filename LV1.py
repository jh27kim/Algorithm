def solution(N, stages):
    answer = []
    completedPlayers = [0 for _ in range(N+2)]
    currentPlayers = [0 for _ in range(N+2)]
    for stage in stages:
        for i in range(1, stage+1):
            completedPlayers[i] += 1
        currentPlayers[stage] += 1
    print(completedPlayers)
    print(currentPlayers)
    for j in range(1, len(completedPlayers)-1):
        answer.append([j,currentPlayers[j] / completedPlayers[j]])
    answer.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in answer]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
