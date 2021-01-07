T = int(input())
gears = [list(input()) for _ in range(T)]
K = int(input())
rotations = [list(map(int, input().split())) for _ in range(K)]


def rotate(c, r):
    #print("gear:", c, "rota: ", r)
    global gears
    if r == 1:
        gears[c] = list(gears[c][-1]) + gears[c][0:-1]
    else:
        gears[c] = gears[c][1:] + list(gears[c][0])


for g, d in rotations:
    junctions = [False for _ in range(T - 1)]
    nodes = []
    for gear in gears:
        nodes.append(gear[6])
        nodes.append(gear[2])

    #print(nodes)
    #print(gears)
    for i in range(1, len(nodes)-1, 2):
        if nodes[i] != nodes[i+1]:
            junctions[(i-1)//2] = True
    right, left = g-1, g-2
    #print(junctions)
    rotate(g - 1, d)
    rr, rl = d, d
    while right < len(junctions):
        rr = rr*(-1)
        if not junctions[right]:
            break
        #print(right+1)
        rotate(right+1, rr)
        right += 1

    while left >= 0:
        rl = rl*(-1)
        if not junctions[left]:
            break
        rotate(left, rl)
        left -= 1

#print(gears)
print(sum(int(i[0]) for i in gears))
