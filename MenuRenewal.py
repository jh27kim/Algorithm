from collections import defaultdict


def combination(cuisines, queue, start, c, temp):
    if len(temp) == c:
        queue.append(temp[:])
        return

    for i in range(start, len(cuisines)):
        temp.append(cuisines[i])
        combination(cuisines, queue, i+1, c, temp)
        temp.pop()

    return queue


def solution(orders, course):
    answer = []
    dishes = defaultdict(int)

    for x in range(len(orders)):
        orders[x] = sorted(list(orders[x]))

    for c in course:
        for i in range(len(orders)):
            if len(orders[i]) >= c:
                candidates = combination(orders[i], [], 0, c, [])
            else:
                continue

            for cand in candidates:
                dishes["".join(cand)] += 1
            print(candidates)

        maximum = -1
        print(dishes)
        for k, v in sorted(dishes.items(), key=lambda x: -x[1]):
            if (maximum != -1 and maximum != v) or v < 2:
                break
            answer.append(k)
            maximum = v

        dishes = defaultdict(int)

    return sorted(answer)


orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
print(solution(orders, course))
