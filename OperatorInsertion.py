import sys

N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
a, b = sys.maxsize, -sys.maxsize
queue = []


def cal():
    start = num[0]
    #print(queue)
    for j in range(len(queue)):
        if queue[j] == 0:
            start += num[j+1]
        elif queue[j] == 1:
            start -= num[j+1]
        elif queue[j] == 2:
            start *= num[j+1]
        elif queue[j] == 3:
            if start > 0:
                start = start // num[j+1]
            else:
                start = -(abs(start) // num[j+1])
    return start


def dfs(depth):
    global a, b
    if depth == N-1:
        result = cal()
        a = min(a, result)
        b = max(b, result)
        return

    for i in range(len(op)):
        if op[i]:
            op[i] -= 1
            queue.append(i)
            dfs(depth+1)
            queue.pop()
            op[i] += 1


dfs(0)
print(b)
print(a)
