N = input()
mid = len(N) // 2
left = sum([int(N[i]) for i in range(mid)])
right = sum([int(N[i]) for i in range(mid, len(N))])
if left == right:
    print('LUCKY')
else:
    print('READY')
