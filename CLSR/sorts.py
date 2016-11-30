#!/usr/bin/env python
import math
from helpers import CLSR_logger

CLSR_logger.curMod(__name__)

def insertionSort(array, desc=False):
    CLSR_logger.info("Insertion Sorting array")
    counter = 0
    i = 0
    for j in range(1, len(array)):
        counter += 1
        key = array.pop(j)
        i = j-1
        CLSR_logger.arraySelects(array, i, j)
        if desc:
            while i >= 0 and array[i] < key:
                counter += 1
                # note that POP happens before INSERT so the index shifts!
                CLSR_logger.arraySelects(array, i, j)
                array.insert(i, array.pop(i))
                i = i-1
            array.insert(i+1, key)
        else:
            while i >= 0 and array[i] > key:
                counter += 1
                # note that POP happens before INSERT so the index shifts!
                CLSR_logger.arraySelects(array, i, j)                
                array.insert(i, array.pop(i))
                i = i-1
            array.insert(i+1,key)

    CLSR_logger.info("Insertion sorted array of length %r" % len(array))
    CLSR_logger.info("Sorted the array in %r steps" % counter)
    CLSR_logger.info("Sorted array is: %r" % str(array))
    return(array)

def selectionSort(array):
    CLSR_logger.info("Selection Sorting array of length %r to Ascending order" % len(array))
    counter = 0
    j = 0
    minval = array[j]
    for j in range(0, len(array)):
        midx = j
        minval = array[j]
        for i in range(j, len(array)):
            counter += 1
            if array[i] < minval:
                minval = array[i]
                midx = i
        switch = array[j]
        array[midx] = switch
        array[j] = minval
        
    CLSR_logger.info("Select sorted array of length %r" % len(array))
    CLSR_logger.info("Sorted the array in %r steps" % counter)
    CLSR_logger.info("Sorted array is: %r" % str(array))
    return(array)

def bubbleSort(array):
    CLSR_logger.info("Bubble sorting array of length %r" % len(array))
    counter = 0
    for i in range(0, len(array)-2):
        for j in range(len(array)-1, i+1, -1):
            counter += 1
            if array[j] < array[i]:
                swap1 = array[j]
                swap2 = array[i]
                array[i] = swap1
                array[j] = swap2
    CLSR_logger.info("Bubble sorted array of length %r" % len(array))
    CLSR_logger.info("Sorted the array in %r steps" % counter)
    CLSR_logger.info("Sorted array is: %r" % str(array))

def mergeSort(array):
    if len(array) > 1:
        midl = math.ceil(len(array)/2)
        larray = mergeSort(list(array[:midl]))
        rarray = mergeSort(list(array[midl:]))
        tarray = larray + rarray
        CLSR_logger.info("Sorted array is: %r" % str(tarray))
        return helpers.merge(tarray)
    return array

def quicksort(array):
    sIdx = 0
    eIdx = len(array)-1
    mIdx = helpers.partition(array, sIdx, eIdx)
    subStack = [sIdx, mIdx, eIdx]
    
    while(len(subStack)>1):
        eIdx = subStack.pop()
        sIdx = subStack.pop()
        if sIdx+2 < eIdx and mIdx != helpers.partition(array, sIdx, eIdx):
            mIdx = helpers.partition(array, sIdx, eIdx)
            print("Pivot value now is %r" % array[mIdx])
            subStack.append(sIdx)
            subStack.append(mIdx)
            subStack.append(eIdx)
        else:
            subStack.append(sIdx)

def countingSort(array, lim):
    arrayB = [0]*(len(array))
    arrayC = [0]*(lim+1)
    for i in range(0, len(array)):
        arrayC[array[i]]= arrayC[array[i]]+1
    for j in range(0, lim+1):
        arrayC[j] = arrayC[j] + arrayC[j-1]
    for i in range(len(array)-1, 0, -1):
        arrayB[arrayC[array[i]]-1] = array[i]
        arrayC[array[i]] = arrayC[array[i]]-1
    return arrayB
