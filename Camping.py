import sys

cnt = 1
while True:
    L, P, V = map(int, sys.stdin.readline().split())
    if L+P+V == 0:
        break
    q, r = divmod(V, P)
    if r <= L:
        print("Case %d: %d" % (cnt, (q*L + r)))
    else:
        print("Case %d: %d" % (cnt, (q*L + L)))
    cnt += 1

