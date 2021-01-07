row, col = map(int, input().split())
cuts = int(input())
row_cuts = [0, col]
col_cuts = [0, row]
r, c = [], []

for i in range(cuts):
    direction, line = map(int, input().split())
    if direction == 0:
        row_cuts.append(line)
    else:
        col_cuts.append(line)

row_cuts.sort()
col_cuts.sort()

for j in range(1, len(row_cuts)):
    r.append(row_cuts[j] - row_cuts[j-1])

for k in range(1, len(col_cuts)):
    c.append(col_cuts[k] - col_cuts[k-1])

print(max(r) * max(c))
