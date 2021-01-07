N, C = map(int, input().split())
nums = list(map(int, input().split()))
freq = dict()

for num in nums:
    if num not in freq:
       freq[num] = 1
    else:
        freq[num] += 1

freq = {k:v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}

for k, v in freq.items():
    for j in range(v):
        print(k, end=" ")