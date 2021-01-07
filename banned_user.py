import itertools

def solution(user_id, banned_id):
    cases = []
    for i in range(len(banned_id)):
        temp = []
        for j in range(len(user_id)):
            if len(banned_id[i]) != len(user_id[j]):
                continue
            else:
                if match(banned_id[i], user_id[j]):
                    temp.append(j)
        cases.append(temp)
    return generator(cases)


def match(ban, usr):
    for i in range(len(ban)):
        if ban[i] == '*':
            continue
        elif ban[i] != usr[i]:
            return False
    return True


def generator(cases):
    result = []
    for case in list(itertools.product(*cases)):
        #print(set(case), len(banned_id))
        if len(set(case)) == len(banned_id):
            result.append(case)
    return len(set(tuple(sorted(x)) for x in result))


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))