from collections import defaultdict


def dfs(cnt, scoreDic, P):
    if cnt == 6:  # 소팅하는부분
        sortDic = sorted(list(scoreDic.items()), key=lambda k: k[1], reverse=True)

        if sortDic[0][1] == sortDic[1][1] == sortDic[2][1] == sortDic[3][1]:  # 상위 4개가 똑같은경우 0.25, 0.25, 0.25. 0.25 4명동점
            ansDic[sortDic[0][0]] += P * 1 / 2
            ansDic[sortDic[1][0]] += P * 1 / 2
            ansDic[sortDic[2][0]] += P * 1 / 2
            ansDic[sortDic[3][0]] += P * 1 / 2
            return


        elif sortDic[0][1] > sortDic[1][1] == sortDic[2][1] == sortDic[3][1]:  # 2 3 4 등이 똑같을 수도 3명동점
            ansDic[sortDic[0][0]] += P
            ansDic[sortDic[1][0]] += P * 1 / 3
            ansDic[sortDic[2][0]] += P * 1 / 3
            ansDic[sortDic[3][0]] += P * 1 / 3
            return

        # elif sortDic[0][1] == sortDic[1][1] == sortDic[2][1] > sortDic[3][1] :#상위 3개가 똑같은 경우 0.3333,0.3333,0.3333, 0 3명동점
        elif sortDic[0][1] == sortDic[1][1] == sortDic[2][1]:  # 상위 3개가 똑같은 경우 0.3333,0.3333,0.3333, 0 3명동점
            ansDic[sortDic[0][0]] += P * (2 / 3)
            ansDic[sortDic[1][0]] += P * (2 / 3)
            ansDic[sortDic[2][0]] += P * (2 / 3)
            ansDic[sortDic[3][0]] += P * 0.0
            return

        # elif sortDic[0][1] > sortDic[1][1] == sortDic[2][1] > sortDic[3][1]:#2위 3위가 똑같은 경우 1, 0.5, 0.5, 0 2명동점

        elif sortDic[0][1] > sortDic[1][1] == sortDic[2][1]:  # 2위 3위가 똑같은 경우 1, 0.5, 0.5, 0 2명동점
            ansDic[sortDic[0][0]] += P
            ansDic[sortDic[1][0]] += P * 0.5
            ansDic[sortDic[2][0]] += P * 0.5
            ansDic[sortDic[3][0]] += P * 0.0
            return

        else:  # 그 외는 1, 1, 0 ,0
            # 1=2,3,4 / 1,2,3=4/ 1,2,3,4
            ansDic[sortDic[0][0]] += P
            ansDic[sortDic[1][0]] += P
            ansDic[sortDic[2][0]] += P * 0.0
            ansDic[sortDic[3][0]] += P * 0.0
            return

    # A가 이길 때
    scoreDic[stringList[cnt][0]] += 3  # A

    dfs(cnt + 1, scoreDic, P * float(stringList[cnt][2]))  # dfs 파라미터에 scoreDic이 들어가는 이유를 제대로 알자!!

    scoreDic[stringList[cnt][0]] -= 3  # A

    # 비길때
    scoreDic[stringList[cnt][0]] += 1  # A
    scoreDic[stringList[cnt][1]] += 1  # B

    dfs(cnt + 1, scoreDic, P * float(stringList[cnt][3]))

    scoreDic[stringList[cnt][0]] -= 1  # A
    scoreDic[stringList[cnt][1]] -= 1  # B

    # A가 질 때
    scoreDic[stringList[cnt][1]] += 3  # B

    dfs(cnt + 1, scoreDic, P * float(stringList[cnt][4]))

    scoreDic[stringList[cnt][1]] -= 3  # B


teams = input().split()
stringList = []

scoreDic = defaultdict(int)
ansDic = defaultdict(int)

for i in range(6):
    stringList.append(list(map(str, input().split())))

for t in teams:
    scoreDic[t] = 0
    ansDic[t] = 0


dfs(0, scoreDic, 1)

for key in scoreDic:
    print(ansDic[key])