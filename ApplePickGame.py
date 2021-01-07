n,m = map(int, input().split())
j = int(input())

apples = [int(input()) for _ in range(j)]
left = 1
size  = m-1
right = left + size
count = 0

for apple in apples:
    if left <= apple <= right:
        continue
    if apple < left:
        count += abs(left - apple)
        left = apple
        right = left + size
    if apple > right:
        count += abs(right-apple)
        right = apple
        left = right - size

print(count)
