import sys
import heapq
'''
N = int(input())
meetings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
priorities = []
answer = 0

for i in meetings:
    heapq.heappush(priorities, (sum(i), i[0], i[1]))

while priorities:
    _, x, y = heapq.heappop(priorities)
    answer += 1
    while priorities:
        if x < priorities[0][0] <= y or x <= priorities[0][1] < y:
            heapq.heappop(priorities)
        else:
            break
            '''

answer = 1
N = int(input())
meetings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

meetings.sort(key=lambda x: (x[1], x[0]))
end = meetings[0][1]

for i in range(1, len(meetings)):
    if meetings[i][0] >= end:
        answer += 1
        end = meetings[i][1]

print(answer)
