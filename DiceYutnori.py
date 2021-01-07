import time
import sys
start_time = time.time()

num = list(map(int, input().split()))
rook = list(range(4))
queue = []
route = [[i for i in range(1, 41) if i % 2 == 0],
         [13, 16, 19, 25, 30, 35, 40, 0],
         [22, 24, 25, 30, 35, 40, 0],
         [28, 27, 26, 25, 30, 35, 40, 0]]

route[0].append(True)
answer = -sys.maxsize


def move():
    #[현재 길, 현재 index]
    score = 0
    result = [[0, 0], [0, 0], [0, 0], [0, 0]]
    cursor = [0, 0, 0, 0]
    #print(queue)
    for j in range(10):
        if result[queue[j]][0] == -1:
            return -1

        rt, ind = result[queue[j]]

        #queue[j] 도착
        if ind+num[j]-1 >= len(route[rt]):
            #print(ind)
            ind = len(route[rt])-num[j]
            #print('arrived', ind)


        #도착지점 말 존재
        if route[rt][ind+num[j]-1] in cursor:
            if route[rt][ind+num[j]-1] != 0:
                return -1

        score += route[rt][ind+num[j]-1]
        cursor[queue[j]] = route[rt][ind + num[j] - 1]
        if result[queue[j]][1] + num[j] >= len(route[rt]):
            result[queue[j]][1] = len(route[rt])-1
        else:
            result[queue[j]][1] += num[j]


        #지름길 선택
        #print(rt, result[queue[j]][1]-1, "haha")
        if route[rt][result[queue[j]][1]-1] % 10 == 0 and route[rt][result[queue[j]][1]-1] != 40:
            result[queue[j]][0] = route[rt][result[queue[j]][1]-1] // 10
            result[queue[j]][1] = 0
        #print(score)
    #print(score, "one loop")
    return score


def comb(d):
    global answer
    if d == 10:
        answer = max(answer, move())
        return
    for i in rook:
        queue.append(i)
        comb(d+1)
        queue.pop()

print('start')
comb(0)



end_time = time.time()
print(answer)
print(end_time-start_time)
