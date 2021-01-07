def hanoi(answer, from_pos, aux_pos, to_pos, n):
    if n == 1:
        answer.append([from_pos, to_pos])
        print(answer, "appended")
        return
    else:
        hanoi(answer, from_pos, to_pos, aux_pos, n-1)
        answer.append([from_pos, to_pos])
        hanoi(answer, aux_pos, from_pos, to_pos, n-1)
    print(answer)
    return answer


def solution(n):
    answer = []
    from_pos, aux_pos, to_pos = 1, 2, 3
    answer = hanoi(answer, from_pos, aux_pos, to_pos, n)
    return answer


n = 4
print(solution(n))