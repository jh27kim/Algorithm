lst = [[1,1,1], [1,0,1]]
R = 2
C = 3

lst2 = [[lst[R-1-i][j] for i in range(R)] for j in range(C)]
print(lst2)

R,C = C, R
lst3 = [[lst2[R-1-i][j] for i in range(R)] for j in range(C)]
print(lst3)