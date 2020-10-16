#!/usr/bin/env python3

def insertionSort(array):
    length = len(array)
    for i in range(1, length):
        key = array[i]
        j = i - 1
        # compare key with previous items as long as it is smaller than them
        while j >= 0 and key < array[j]:
            # shift item if key is smaller
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array

itemlist = [24,6,1,5,22,3,2,18,10,8,7,15]
print(insertionSort(itemlist))