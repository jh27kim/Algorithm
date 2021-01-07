##Selection Sort
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    minidx = i
    for j in range(i+1, len(array)):
        if array[j] < array[minidx]:
            minidx = j
    array[minidx], array[i] = array[i], array[minidx]
print(array)


##Insertion sort
newArray = []
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    if not newArray:
        newArray.append(array[i])
        continue
    for j in range(len(newArray)):
        if newArray[j] > array[i]:
            newArray.insert(j, array[i])
            break
print(newArray)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end

    while left <= right:
        while left <= end and array[left] < array[pivot]:
            left += 1
        while right > start and array[right] > array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, len(array)-1)
print(array)

def quick_sort(array):
    if len(array) <= 1:
        return array
    print(array)
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

"""


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left1 = merge_sort(left)
    right1 = merge_sort(right)
    return merge(left1, right1)


def merge(array1, array2):
    i, j= 0, 0
    array = []

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            array.append(array1[i])
            i += 1
        else:
            array.append(array2[j])
            j += 1

    while i < len(array1):
        array.append(array1[i])
        i += 1

    while j < len(array2):
        array.append(array2[j])
        j += 1
    return array


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(array)
print(merge_sort(array))
