#!/usr/bin/env python3

def bubbleSort(itemList):
    length = len(itemList)
    for i in range(length):
        for j in range(length-1):
            if itemList[j] > itemList[j+1]:
                temp = itemList[j]
                itemList[j] = itemList[j+1]
                itemList[j+1] = temp
    return itemList


print(bubbleSort([5,4,3,2,1])) # worst case => time complexity: O(n^2 - n) = O(n^2)
