def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        visited = [0 for _ in range(len(skill))]
        done = True
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skill:
                ind = skill.index(skill_trees[i][j])
                visited[ind] = 1
                if not(all(visited[:ind])):
                    done = False
                    break
        if done:
            answer += 1
    return answer

print(all([1,1,0]))
skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))