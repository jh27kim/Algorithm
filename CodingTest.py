from collections import deque

CODING_STUDY = [0, 0, 0, 1, 1]
ALGO_STUDY = [0, 0, 1, 0, 1]


def solution(alp, cop, problems):
    max_alp = -1
    max_cop = -1
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)

    problems += [CODING_STUDY]
    problems += [ALGO_STUDY]

    queue = deque()
    queue.appendleft((alp, cop, 0))
    answer = 1e9
    while queue:
        cur_alp, cur_cop, cur_cost = queue.popleft()
        print(cur_alp, cur_cop, cur_cost)
        if cur_cost > answer:
            continue
        if cur_alp >= max_alp and cur_cop >= max_cop:
            answer = min(answer, cur_cost)
        for i in range(len(problems)):
            alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[i]
            if alp_req <= cur_alp and cop_req <= cur_cop:
                queue.append((cur_alp + alp_rwd, cur_cop + cop_rwd, cur_cost + cost))

    return answer


alp = 10
cop = 10
problems = [[10,15,2,1,2],[20,20,3,3,4]]
print(solution(alp, cop, problems))