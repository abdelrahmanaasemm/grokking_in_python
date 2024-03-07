def partion(list, start, end):
    pivot = list[end]
    swapIndex = start - 1
    for i in range(start , end):
        if pivot > list[i]:
            swapIndex += 1
            list[swapIndex], list[i] = list[i], list[swapIndex]
    swapIndex += 1
    list[swapIndex], list[end] = list[end], list[swapIndex]
    return swapIndex


def quicksort(list, start, end):
    if start < end:
        pivot = partion(list, start, end)
        quicksort(list, pivot + 1, end)
        quicksort(list, start, pivot - 1)
        return list

list = [1, 2, 4, 3, 0, 77, 11, 44, 9, 6, 5]
quicksort(list, 0, len(list) - 1)
print(list)