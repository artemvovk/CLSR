#!/usr/bin/env python
from helpers import CLSR_logger, partition

CLSR_logger.curMod(__file__)

def linearSearch(array, find):
    CLSR_logger.info("Linear Searching for %r" % find)
    for j in range(0, len(array)-1):
        if array[j] == find:
            CLSR_logger.info("Found %r at index %r" % (array[j], j))
            return j
    CLSR_logger.info("Not found")     


def getMaxCrossSubarray(array):
    CLSR_logger.info("Getting Crossing Subarray for %r" % array)
    if len(array) == 1:
        return array[0]
    lsum = array[0]
    tsum = 0
    mleft = 0
    for i in range(math.ceil(len(array)/2), 0, -1):
        tsum = tsum + array[i]
        if tsum > lsum:
            lsum = tsum
            mleft = i
    rsum = array[0]
    tsum = 0
    mright = 0
    for j in range(math.ceil(len(array)/2)+1, len(array)):
        tsum = tsum + array[j]
        if tsum > rsum:
            rsum = tsum
            mright = j
    CLSR_logger.info("We got max crossing subarray at %r to %r with sum of %r" % (mleft, mright, lsum+rsum))
    return lsum+rsum

def getMaxSubarray(array):
    CLSR_logger.info("Getting Max Subarray for %r" % array)
    if len(array) == 1:
        return array[0]
    else:
        midl = math.ceil(len(array)/2)
        lsum = getMaxSubarray(array[:midl])
        rsum = getMaxSubarray(array[midl:])
        msum = getMaxCrossSubarray(array)

        if lsum >= rsum and lsum >= msum:
            CLSR_logger.info("We got left sum at %r" % (lsum))
            return lsum
        elif rsum >= lsum and rsum >= msum:
            CLSR_logger.info("We got right sum at %r" % (rsum))
            return rsum
        else:
            CLSR_logger.info("We got mid sum at %r" % (msum))
            return msum

def randomSearch(array, find):
    CLSR_logger.info("Random Searching for %r" % find)
    n = len(array)
    barray = list()
    i = random.randrange(0,n)
    steps = 0

    while array[i] != find:
        
        i = random.randrange(0,n)
        steps += 1
        if len(barray) == len(array) or steps == n*n:
            CLSR_logger.info("Didn't find %r in the array in %r steps" % (find, steps))
            return -1

        if array[i] not in barray:
            CLSR_logger.info("Length of one is %r and length of other is %r" % (len(array), len(barray)))
            barray.append(array[i])
            
        
    CLSR_logger.info("Found %r at %r" % (find, i))
    return i

def deterministicSearch(array, find):
    CLSR_logger.info("Deterministic Searching for %r" % find)
    n = len(array)
    for i in range(0,n):
        if array[i] == find:
            CLSR_logger.info("Found %r at %r" % (find, i))
            return i
    CLSR_logger.info("Didn't find %r in %r" % (find, array))
    return -1

def findMinMax(array):
    L = len(array)
    if L % 2 == 0:
        if array[0] < array[1]:
            mMin = array[0]
            mMax = array[1]
        else:
            mMin = array[1]
            mMax = array[0]
    else:
        mMin = array[0]
        mMax = array[0]

    for i in range(2, L-1):
        j = i+1
        if array[i] < array[j]:
            if array[i] < mMin:
                mMin = array[i]
            if array[j] > mMax:
                mMax = array[j]
        else:
            if array[j] < mMin:
                mMin = array[j]
            if array[i] > mMax:
                mMax = array[i]
    return (mMin, mMax)
                
def randomizedSelect(array, sIdx, eIdx, i):
    if sIdx == eIdx:
        return array[0]
    pivot = helpers.partition(array, sIdx, eIdx)
    k = pivot-sIdx+1
    if i == k:
        return array[pivot]
    elif i < k:
        return randomizedSelect(array, sIdx, pivot-1, i)
    else:
        return randomizedSelect(array, pivot+1, eIdx, i-k)

def weightedMedian(warray):
    warray.sort(key=lambda tup: tup[0])
    sumW = 0
    for item in warray:
        sumW += item[1]
    return sumW
