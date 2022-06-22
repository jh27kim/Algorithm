applicants = {"1": [], "2": [], "3": []}


def solution(region, num, info):
    answer = [-1 for _ in range(len(info))]
    for i in range(len(info)):
        _area, _no_house_year, _registered_year, _supporting_family = info[i]
        _score = (_no_house_year + 1) * 2 + (_registered_year + 2) + (_supporting_family + 1) * 5
        applicants[str(_area)].append([_score, i])

    target = applicants[str(region)]
    target.sort(key=lambda x: (-x[0], x[1]))

    rest = []
    for i in range(1, 4):
        if i != region:
             rest.extend(applicants[str(i)])

    rest.sort(key=lambda x: (-x[0], x[1]))
    target.extend(rest)

    #print(target)

    for i in range(num):
        _s, _i = target[i]
        answer[_i] = i + 1

    return answer


region = 1
num = 7
info = 	[[1, 0, 2, 1], [2, 6, 5, 2], [3, 10, 2, 4], [1, 1, 5, 6], [2, 7, 10, 2], [3, 8, 6, 3]]
print(solution(region, num, info))
