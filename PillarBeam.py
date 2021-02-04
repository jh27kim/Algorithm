def impossible(result):
    COL, ROW = 0, 1
    for x, y, a in result:
        if a == COL:
            if y != 0 and (x, y-1, COL) not in result and (x-1, y, ROW) not in result \
                and (x, y, ROW) not in result:
                return True
        else:
            if (x, y-1, COL) not in result and (x+1, y-1, COL) not in result \
                and not((x-1, y, ROW) in result and (x+1, y, ROW) in result):
                return True
    return False


def solution(n, build_frame):
    result = set()

    for x, y, a, build in build_frame:
        item = (x, y, a)
        if build:  # 추가일 때
            result.add(item)
            if impossible(result):
                result.remove(item)
        elif item in result:  # 삭제할 때
            result.remove(item)
            if impossible(result):
                result.add(item)
    answer = list(map(list, result))
    return sorted(answer)


n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
print(solution(n, build_frame))
