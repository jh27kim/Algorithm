import sys
import heapq

N, K = map(int, input().split())
jewel = []
bag = []
gem = []
answer = 0

for _ in range(N):
    weight, value = map(int, sys.stdin.readline().split())
    heapq.heappush(gem, [weight, value])

for _ in range(K):
    capacity = int(sys.stdin.readline())
    heapq.heappush(bag, capacity)

for _ in range(K):
    capacity = heapq.heappop(bag)

    while gem and capacity >= gem[0][0]:  # 현재 bag의 capacity보다 이하인 모든 보석에 관하여
        [weight, value] = heapq.heappop(gem)  # 최소 무게부터 차례대로 꺼낸다
        heapq.heappush(jewel, -value)

    if jewel:
        answer -= heapq.heappop(jewel)
    elif not jewel:
        break

print(answer)
