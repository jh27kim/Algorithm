def solution(clothes):
    answer = 1
    d = dict()
    for cloth, kind in clothes:
        if kind in d:
            d[kind].append(cloth)
        else:
            d[kind] = [cloth]
    for k, v in d.items():
        answer *= len(v)+1
    return answer-1


clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))