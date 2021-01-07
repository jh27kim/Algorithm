from collections import deque

answer = []
result = []

def dfs(end, tickets, v):
    global answer
    if sum(v) == len(tickets):
        return True
    for i in range(len(tickets)):
        if end == tickets[i][0] and not v[i]:
            answer.append(tickets[i][1])
            v[i] = 1
            if dfs(tickets[i][1], tickets, v):
                return True
            v[i] = 0
            answer.pop()


def solution(tickets):
    global answer
    visited = [0 for _ in range(len(tickets))]
    tickets.sort(key=lambda x: x[1])
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            answer.append(tickets[i][1])
            visited[i] = 1
            if dfs(tickets[i][1], tickets, visited):
                answer.insert(0, "ICN")
                return answer
            visited[i] = 0
            answer.pop()
    answer.insert(0, "ICN")
    return answer


tickets = ["ICN", "SFO"]
print(solution(tickets))