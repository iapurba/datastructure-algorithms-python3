#!/usr/bin/env python3

def first_recurring_character(inputList):
    itemDict = {}
    for item in inputList:
        if itemDict.get(item, None) != None:
            return item
        else:
            itemDict[item] = item
    return 'No recurring character'


if __name__ == "__main__":
    inputList = [1,2,3,4,5,3,2,22,10] # return char should be 3
    recurring_char = first_recurring_character(inputList)
    print(recurring_char)
