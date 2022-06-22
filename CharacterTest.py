INDEX = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
SCORE = {"1": 3, "2": 2, "3": 1, "4": 0, "5": 1, "6": 2, "7": 3}


def solution(survey, choices):
    answer = ''
    for i in range(len(survey)):
        x, y = survey[i]
        s = SCORE[str(choices[i])]
        if choices[i] < 4:
            INDEX[x] += s
        else:
            INDEX[y] += s

    if INDEX["R"] >= INDEX["T"]:
        answer += "R"
    else:
        answer += "T"

    if INDEX["C"] >= INDEX["F"]:
        answer += "C"
    else:
        answer += "F"

    if INDEX["J"] >= INDEX["M"]:
        answer += "J"
    else:
        answer += "M"

    if INDEX["A"] >= INDEX["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer

# survey [비동의, 동의]
# choices [매우 비동의, 비동의, 약간 비동의, 모르겠음, 약간 도으이, 동의, 매우 동의]

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))