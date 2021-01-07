def solution(priorities, location):
    answer = 0
    idx = [i for i in range(len(priorities))]

    while priorities:
        candidate = priorities.pop(0)
        loc = idx.pop(0)
        if candidate >= max(priorities):
            answer += 1
            if loc == location:
                return answer
        else:
            priorities.append(candidate)
            idx.append(loc)


priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))