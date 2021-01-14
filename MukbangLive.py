import heapq

def solution(food_times, k):
    q = []
    if sum(food_times) <= k:
        return -1
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0
    prev = 0
    length = len(q)
    while sum_value + ((q[0][0] - prev) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now-prev) * length
        length -= 1
        prev = now
    q.sort(key=lambda x:x[1])

    return (q[(k-sum_value)%length][1])


food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))
