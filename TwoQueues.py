def solution(queue1, queue2):
    target = (sum(queue1) + sum(queue2)) / 2
    total_queue = queue1 + queue2
    queue = [0 for _ in range(len(total_queue))]
    queue[0] = total_queue[0]
    for i in range(1, len(queue)):
        queue[i] = total_queue[i] + queue[i-1]
    queue = [0] + queue

    answer = 0
    i, j = 0, len(queue)//2
    while j < len(queue):
        if queue[j] - queue[i] > target:
            i += 1
        elif queue[j] - queue[i] < target:
            j += 1
        else:
            if i > len(queue)//2:
                forehead = i - len(queue)//2
                answer += forehead
                answer += len(queue)//2 + forehead
                answer += j-i
            else:
                answer += i
                answer += abs(len(queue)//2 - j)

            return answer

    return -1


queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]
print(solution(queue1, queue2))


#  [3, 2, 7, 2, 4, 6, 5, 1]