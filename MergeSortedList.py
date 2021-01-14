n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

i, j = 0, 0
result = []

while i < n or j < m:
    if j >= m or (i < n and a[i] <= b[j]):
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

print(result)