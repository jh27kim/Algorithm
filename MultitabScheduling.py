N, K = map(int, input().split())
use_order = list(map(int, input().split()))
'''
usages = defaultdict(int)
plug = []
answer = 0
included = set()

for i in use_order:
    if not usages[i]:
        usages[i] = 1
    else:
        usages[i] += 1


for i in range(len(use_order)):
    #print(included, plug)
    if use_order[i] in included:
        continue

    if len(plug) == N and use_order[i] not in included:
        _, x = heapq.heappop(plug)
        included.remove(x)
        answer += 1
    usages[use_order[i]] -= 1
    heapq.heappush(plug, (usages[use_order[i]], use_order[i]))
    included.add(use_order[i])

print(answer)
'''

plug = []
answer = 0

for i in range(K):
    if use_order[i] in plug:
        continue

    if len(plug) < N:
        plug.append(use_order[i])
        continue

    idxs = []
    for j in range(len(plug)):
        try:
            idx = use_order[i:].index(plug[j])
        except:
            idx = 101
        idxs.append(idx)

    evict = idxs.index(max(idxs))
    del plug[evict]
    plug.append(use_order[i])
    answer += 1

print(answer)
