N = int(input())
scoreA = 0
scoreB = 0
times = [[0, 0]]
winning = [0]
timeA = 0
timeB = 0
intervals = []

for i in range(N):
    team, time = input().split()
    M, S = time.split(":")
    times.append([M, S])
    if team == "1":
        scoreA += 1
    else:
        scoreB += 1

    if scoreA > scoreB:
        winning.append(1)
    elif scoreB > scoreA:
        winning.append(2)
    elif scoreB == scoreA:
        winning.append(0)

times.append(['48', '00'])

for l in range(1, len(times)):
    nmin = int(times[l][0]) - int(times[l-1][0])
    nsec = int(times[l][1]) - int(times[l - 1][1])
    if nsec < 0:
        nmin -= 1
        nsec += 60
    intervals.append([nmin, nsec])

for j in range(len(winning)):
    if winning[j] == 1:
        timeA += intervals[j][0] * 60 + intervals[j][1]
    elif winning[j] == 2:
        timeB += intervals[j][0] * 60 + intervals[j][1]

print(str(timeA//60).zfill(2)+":"+str(timeA % 60).zfill(2))
print(str(timeB//60).zfill(2)+":"+str(timeB % 60).zfill(2))
