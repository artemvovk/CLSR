#!/usr/bin/env python
import math
from helpers import CLSR_logger, merge, partition
from dataStructures import *

CLSR_logger.curMod(__name__)

def insertionSort(array, desc=False):
    CLSR_logger.info("Insertion Sorting the array")
    i = 0
    for j in range(1, len(array)):
        key = array.pop(j)
        i = j-1
        if desc:
            while i >= 0 and array[i] < key:
                # note that POP happens before INSERT so the index shifts!
                array.insert(i, array.pop(i))
                i = i-1
            array.insert(i+1, key)
        else:
            while i >= 0 and array[i] > key:
                # note that POP happens before INSERT so the index shifts!
                array.insert(i, array.pop(i))
                i = i-1
            array.insert(i+1,key)
    CLSR_logger.info("Sorted array is: %r" % str(array))
    return(array)

def selectionSort(array, desc=False):
    CLSR_logger.info("Selection Sorting the array")
    j = 0
    if desc:
        maxval = array[j]
        for j in range(0, len(array)):
            midx = j
            maxval = array[j]
            for i in range(j, len(array)):
                if array[i] > maxval:
                    maxval = array[i]
                    midx = i
                switch = array[j]
                array[midx] = switch
                array[j] = maxval
    else:
        minval = array[j]
        for j in range(0, len(array)):
            midx = j
            minval = array[j]
            for i in range(j, len(array)):
                if array[i] < minval:
                    minval = array[i]
                    midx = i
                switch = array[j]
                array[midx] = switch
                array[j] = minval
    CLSR_logger.info("Sorted array is: %r" % str(array))
    return(array)

def bubbleSort(array, desc=False):
    CLSR_logger.info("Bubble sorting the array")
    for i in range(0, len(array)-2):
        for j in range(len(array)-1, i+1, -1):
            if desc and array[j] > array[i]:
                swap1 = array[j]
                swap2 = array[i]
                array[i] = swap1
                array[j] = swap2
            elif array[j] < array[i]:
                swap1 = array[j]
                swap2 = array[i]
                array[i] = swap1
                array[j] = swap2
    CLSR_logger.info("Sorted array is: %r" % str(array))
    return array

def mergeSort(array, sIdx=0, eIdx=-1, desc=False):
    CLSR_logger.info("Merge Sorting array")
    if eIdx == -1:
        eIdx = len(array)
    if eIdx-sIdx > 1:
        mIdx = math.ceil((eIdx+sIdx)/2)
        mergeSort(array, sIdx, mIdx)
        mergeSort(array, mIdx, eIdx)
        return merge(array, sIdx, mIdx, eIdx)
    CLSR_logger.info("Sorted array is: %r" % str(array))
    return array

def heapSort(array, desc=False):
    CLSR_logger.info("Heap Sorting array")
    heap = Heap(array)
    if desc:
        heap.buildMinHeap()
        for i in range(heap.heapSize-1, -1, -1):
            heap.nodes[0], heap.nodes[i] = heap.nodes[i], heap.nodes[0]
            heap.heapSize -= 1
            heap.minHeapify()        
    else:
        heap.buildMaxHeap()
        for i in range(heap.heapSize-1, -1, -1):
            heap.nodes[0], heap.nodes[i] = heap.nodes[i], heap.nodes[0]
            heap.heapSize -= 1
            heap.maxHeapify()
    array = heap.nodes
    CLSR_logger.info("Sorted array is: %r" % str(array))
    return array


def quicksort(array, sIdx=0, eIdx=-1):
    CLSR_logger.info("Quick Sorting array")
    if eIdx == -1:
        eIdx = len(array)-1
    
    mIdx = partition(array, sIdx, eIdx)
    CLSR_logger.info("Start: {}, Mid: {}, End: {}".format(sIdx, mIdx, eIdx))
    subStack = [sIdx, mIdx, eIdx]

    while len(subStack) > 1:
        eIdx = subStack.pop()
        sIdx = subStack.pop()
        mIdx = partition(array, sIdx, eIdx)
        CLSR_logger.info("Start: {}, End: {}".format(sIdx, eIdx))
        if mIdx-1 > sIdx:
            CLSR_logger.info("Mid: {}".format(mIdx))
            subStack.append(sIdx)
            subStack.append(mIdx-1)
        if mIdx+1 < eIdx:
            CLSR_logger.info("Mid: {}".format(mIdx))
            subStack.append(mIdx+1)
            subStack.append(eIdx)
    CLSR_logger.info("Sorted array is: %r" % str(array))
    return array

def countingSort(array, lim):
    CLSR_logger.info("Count Sorting array")
    arrayB = [0]*(len(array))
    arrayC = [0]*(lim+1)
    for i in range(0, len(array)):
        arrayC[array[i]]= arrayC[array[i]]+1
    for j in range(0, lim+1):
        arrayC[j] = arrayC[j] + arrayC[j-1]
    for i in range(len(array)-1, 0, -1):
        arrayB[arrayC[array[i]]-1] = array[i]
        arrayC[array[i]] = arrayC[array[i]]-1
    CLSR_logger.info("Sorted array is: %r" % str(array))
    return array  

