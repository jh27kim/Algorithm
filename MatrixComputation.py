import numpy as np


def shift(rc, c):
    return np.roll(rc[0], c, axis=0)


def rotate(rc, c):
    return rc


def solution(rc, operations):
    answer = [[]]
    seq = []
    i, j = 0, 0
    cnt = 0
    operations.append("FIN")
    while j < len(operations):
        if operations[j] == operations[i]:
            j += 1
            cnt += 1
        else:
            seq.append([operations[i], cnt])
            i = j
            cnt = 0

    for op, cnt in seq:
        cnt %= len(rc)
        if op == "ShiftRow":
            rc = shift(rc, cnt)
        else:
            rc = rotate(rc, cnt)

    return answer


rc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
operations = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]
solution(rc, operations)
