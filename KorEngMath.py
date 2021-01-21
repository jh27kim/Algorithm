N = int(input())

lst = []

for _ in range(N):
    name, kor, eng, math = input().split()
    lst.append([name, int(kor), int(eng), int(math)])

lst.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))

for n in lst:
    print(n[0])
