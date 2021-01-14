n = 10
m = 15
data = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]


n, m = map(int, input().split())
data = list(map(int, input().split()))
answer = int(1e9)
res = 0
end = 0

for start in range(n):
    while res < m and end < n:
        res += data[end]
        end += 1
    if res >= m:
        answer = min(answer, end-start)
    res -= data[start]
print(answer if answer != int(1e9) else 0)
