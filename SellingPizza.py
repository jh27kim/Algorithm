S = int(input())
m, n = map(int, input().split())
A, B = [], []
for _ in range(m):
    A.append(int(input()))
for _ in range(n):
    B.append(int(input()))
answer = 0
combs = []


def select(x, y):
    global answer
    for k in range(len(A)):
        if k+x > len(A):
            a = sum(A[k:]) + sum(A[0:k+x-len(A)])
            #print("exceed A", A[k:], A[0:k+x-len(A)])
        else:
            a = sum(A[k:k+x])
            #print("not exceed A", A[k:k+x])

        for l in range(len(B)):
            if l + y > len(B):
                b = sum(B[l:]) + sum(B[0:l+y-len(B)])
                #print("exceed B", B[l:], B[0:l+y-len(B)])
            else:
                b = sum(B[l:l+y])
                #print("not exceed B", B[l:l+y])
            if a+b == S:
                #combs.append([A[k:k+x], B[l:l+y]])
                answer += 1
            if y == 0:
                break



for i in range(0, len(A)):
    for j in range(0, len(B)):
        select(i, j)

#print(combs)
print(answer)
