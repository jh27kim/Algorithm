def solution(number, k):
    number = list(map(int, number))
    queue = []
    for i in range(len(number)):
        #print(queue, k)
        if queue:
            while queue[-1] < number[i] and k:
                queue.pop()
                k -= 1
                if not queue:
                    break
        queue.append(number[i])

    return queue

a = "a"
number = "4177252841"
k = 4
print(solution(number, k))