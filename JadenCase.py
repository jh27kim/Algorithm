def solution(s):
    answer = ''
    s = s.split(" ")
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j == 0 and s[i][j].islower():
                n = chr(ord(s[i][j]) - 32)
                answer += n
            elif j != 0 and s[i][j].isalpha() and s[i][j].isupper():
                n = chr(ord(s[i][j]) + 32)
                answer += n
            else:
                answer += s[i][j]
        if i != len(s) - 1:
            answer += " "
    return answer



s = "AaAaaA"
print(solution(s))
