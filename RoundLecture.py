import heapq

n = int(input())
universities = [list(map(int, input().split())) for _ in range(n)]
universities.sort(key=lambda x:x[1])
answer = 0
heap = []

for i in range(n):
    answer += universities[i][0]
    heapq.heappush(heap, universities[i][0])
    if len(heap) > universities[i][1]:
        answer -= heapq.heappop(heap)

print(answer)

