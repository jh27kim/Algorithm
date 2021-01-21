def revenue_making(idx, rev):
    global max_rev
    if idx == N:
        if max_rev < rev:
            max_rev = rev
        return
    revenue_making(idx+1, rev) #상담을 안 받는 경우
    if idx + table[idx][0] <= N: #상담을 해줄 수 있는 경우
        revenue_making(idx+table[idx][0], rev+table[idx][1])

N = int(input())
table = []
time = []
price = []
for i in range(N):
    t, p = map(int, input().split())
    table.append((t,p))
    time.append(t)
    price.append(p
                 )
max_rev = 0
revenue_making(0, 0)

dp = [0] * (N+1)
maxvalue = 0

for i in range(N-1, -1, -1):
    dur = i + time[i]
    if dur <= N:
        dp[i] = max(dp[dur]+price[i], maxvalue)
        maxvalue = dp[i]
    else:
        dp[i] = maxvalue

print(maxvalue)
print(max_rev)