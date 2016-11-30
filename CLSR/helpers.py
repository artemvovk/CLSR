#!/usr/bin/env python

# Setting up logger and colorizing for debug output
import logging, types
from colorama import init, Fore, Back, Style


LOG_FORMAT = '\n==' + Fore.YELLOW + '%(asctime)s' + Style.RESET_ALL + ' in ' + Style.BRIGHT + '%(funcName)s' + Style.RESET_ALL + '==\n%(message)s\n'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
CLSR_logger = logging.getLogger(__file__)

def curMod(self, moduleName):
    self.info(Style.RESET_ALL +'Started module: ' + Fore.GREEN + '{}'.format(moduleName) + Style.RESET_ALL + ' ')

def arraySelects(self, array, *indecies):
    strArray = '['
    for i in range(0, len(array)):
         if i in indecies:
             strArray += str(Style.BRIGHT + str(array[i])+Style.RESET_ALL)+','
         else:
             strArray += str(array[i])+','
    strArray = strArray[:-1]+']'
    self.info(strArray)

CLSR_logger.arraySelects = types.MethodType(arraySelects, CLSR_logger)

CLSR_logger.curMod = types.MethodType(curMod, CLSR_logger)


# Random Array Generators:
import math, random

def getRandomArray(length=10, amp=100, neg=False, desc=False, weights=False):
    returnArray = list()
    if neg:        
        returnArray.extend([int(amp*random.uniform(-1,1)) for i in range(length)])
    else:
        returnArray.extend([int(amp*random.uniform(0,1)) for i in range(length)])
    if weights:
        returnArray = [(x,y) for x in returnArray for y in [round(1*random.uniform(0,1), 3) for i in range(length)]]
    if desc:
        returnArray.sort(reverse=True)
    CLSR_logger.info("Generated array: %r" % returnArray)
    return(returnArray)


# Merge and Partition helpers

def merge(array):
    #print("Merge sorting array of length %r" % len(array))
    counter = 0
    if len(array) == 1:
        return array
    midl = math.ceil(len(array)/2)
    larray = list(array[:midl])
    rarray = list(array[midl:])
    larray.append(math.inf)
    rarray.append(math.inf)
    
    for i in range(0, len(array)):
        counter += 1
        if larray[0] < rarray[0] or math.isinf(rarray[0]):
            array[i] = larray.pop(0)
        elif rarray[0] < larray[0] or math.isinf(larray[0]):
            array[i] = rarray.pop(0)
    #print("Merge sorted array of length %r" % len(array))
    #print("Sorted the array in %r steps" % counter)
    #print("Which comes out to %r orders of length" % (math.log(counter, len(array))))
    #print("Sorted array is: %r" % str(array))
    return(array)

def partition(array, sIdx, eIdx):
    
    lIdx = sIdx
    rIdx = eIdx
    iIdx = sIdx+int((eIdx-sIdx)*random.random())

    x = array[iIdx]
    r = array[rIdx]

    array[iIdx], array[rIdx] = r, x


    x = array[eIdx]
    print("Our pivot is %r" % (x))
    i = sIdx-1
    for j in range(sIdx, rIdx+1):
        if array[j] < x:
            i+=1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[rIdx] = array[rIdx], array[i+1]
    print("Pivot now at %r" % (i+1))
    return(i+1)
