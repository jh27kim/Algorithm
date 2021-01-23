def quicksort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[0]
    rest = lst[1:]

    left = [i for i in rest if i < pivot]
    right = [i for i in rest if i >= pivot]

    return quicksort(left) + [pivot] + quicksort(right)


def merge(l, r):
    i, j = 0, 0
    arr = []
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            arr.append(l[i])
            i += 1
        else:
            arr.append(r[j])
            j += 1

    while i < len(l):
        arr.append(l[i])
        i += 1

    while j < len(r):
        arr.append(r[j])
        j += 1

    return arr


def mergesort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2

    left = lst[:mid]
    right = lst[mid:]

    new_left = mergesort(left)
    new_right = mergesort(right)

    return merge(new_left, new_right)



lst = [2, 4, 1, 7, 3]
print(mergesort(lst))
print(quicksort(lst))
