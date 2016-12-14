#!/usr/bin/env python
import math
from .helpers import CLSR_logger, partition

CLSR_logger.curMod(__name__)


def linearSearch(array, find):
    CLSR_logger.info("Linear Searching for %r" % find)
    for j in range(0, len(array)-1):
        if array[j] == find:
            CLSR_logger.info("Found %r at index %r" % (array[j], j))
            return j
    CLSR_logger.info("Not found")     


def getMaxCrossSubarray(array, low=0, mid=-1, high=-1):
    CLSR_logger.info("Getting Crossing Subarray")
    if high == -1:
        high = len(array)
    if mid == -1:
        mid = math.ceil((low+high)/2)
    lsum = -1*math.inf
    tsum = 0
    mleft = 0
    for i in range(mid, low-1, -1):
        tsum = tsum + array[i]
        if tsum > lsum:
            lsum = tsum
            mleft = i
    rsum = -1*math.inf
    tsum = 0
    mright = 0
    for j in range(mid, high):
        tsum = tsum + array[j]
        if tsum > rsum:
            rsum = tsum
            mright = j
    CLSR_logger.info("We got Max Crossing Subarray at %r to %r with sum of %r" % (mleft, mright, lsum+rsum))
    return (mleft, mright, lsum+rsum)

def getMaxSubarray(array, low=0, high=-1):
    CLSR_logger.info("Getting Max Subarray")
    if high == -1:
        high = len(array)
    if high-low <= 1:
        return (low, high, array[low])
    else:
        mIdx = math.ceil((low+high)/2)
        lLow,lHigh,lSum = getMaxSubarray(array, 0, mIdx)
        rLow,rHigh,rSum = getMaxSubarray(array, mIdx, high)
        cLow,cHigh,cSum = getMaxCrossSubarray(array, low, mIdx, high)

        if lSum >= rSum and lSum >= cSum:
            CLSR_logger.info("Middle Corssing array between {} and {} has sum of {}".format(lLow, lHigh, lSum))
            return lLow, lHigh, lSum
        elif rSum >= lSum and rSum >= cSum:
            CLSR_logger.info("Middle Corssing array between {} and {} has sum of {}".format(rLow, rHigh, rSum))
            return rLow, rHigh, rSum
        else:
            CLSR_logger.info("Middle Corssing array between {} and {} has sum of {}".format(cLow, cHigh, cSum))
            return cLow, cHigh, cSum

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
                
def randomizedSelect(array, sIdx=0, eIdx=-1, i=0):
    if eIdx == -1:
        eIdx = len(array)
    if sIdx == eIdx:
        return array[0]
    pivot = partition(array, sIdx, eIdx)
    k = pivot-sIdx
    if i == k:
        return array[pivot]
    elif i < k:
        return randomizedSelect(array, sIdx, pivot-1, i)
    else:
        return randomizedSelect(array, pivot, eIdx, i-k)

def weightedMedian(warray):
    warray.sort(key=lambda tup: tup[0])
    sumW = 0
    for item in warray:
        sumW += item[1]
    return sumW
