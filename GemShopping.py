def solution(gems):
    left = 0
    right = len(gems)
    completed = len(set(gems))
    while True:
        if len(set(gems[left:right])) < completed:
            right += 1
            while True:
                if len(set(gems[left:right])) < completed:
                    return [left, right]
                left += 1
        right -= 1

def solution(gems):
    completed = len(set(gems))
    size = len(gems)
    left, right = 0, 0
    d = {gems[left]:1}
    cand = []
    while left < size and right < size:
        if len(d) < completed:
            right += 1
            if right == len(gems):
                break
            d[gems[right]] = d.get(gems[right], 0) + 1
        else:
            cand.append((right-left, [left+1, right+1]))
            d[gems[left]] = d.get(gems[left], 0) - 1
            if d[gems[left]] == 0:
                del d[gems[left]]
            left += 1
    cand.sort(key = lambda x:x[0])
    return cand[0][1]


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))