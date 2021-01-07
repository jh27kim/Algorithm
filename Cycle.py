import copy
N, P = map(int, input().split())
Next = copy.deepcopy(N)
results = {Next: 1}

while True:
    Next = (Next*N) % P
    if Next not in results:
        results[Next] = 1
    else:
        results[Next] += 1
    if results[Next] > 2:
        print(sum(1 for i in results.values() if i >= 2))
        break
