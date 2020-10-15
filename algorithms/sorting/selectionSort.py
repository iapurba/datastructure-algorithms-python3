#!/usr/bin/env python3

def selectionSort(items):
    length = len(items)
    for i in range(length):
        min = i
        temp = items[i]
        for j in range(i+1, length):
            if items[j] < items[min]:
                min = j
        items[i] = items[min]
        items[min] = temp
    return items


print(selectionSort([23,4,1,6,22,40,61,8,2,34,25,11,7]))
