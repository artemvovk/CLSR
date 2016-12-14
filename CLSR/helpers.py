#!/usr/bin/env python

# Setting up logger and colorizing for debug output
import logging, types
from colorama import init, Fore, Back, Style


LOG_FORMAT = '\n==' + Fore.YELLOW + '%(asctime)s' + Style.RESET_ALL + ' in ' + Style.BRIGHT + '%(funcName)s' + Style.RESET_ALL + '==\n%(message)s\n'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
CLSR_logger = logging.getLogger(__file__)

def curMod(self, moduleName):
    self.info(Style.RESET_ALL +'Started module: ' + Fore.GREEN + '{}'.format(moduleName) + Style.RESET_ALL + ' ')

CLSR_logger.curMod = types.MethodType(curMod, CLSR_logger)

CLSR_logger.info("CLSR_logger started")
CLSR_logger.curMod(__name__)


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
def merge(array, sIdx, mIdx, eIdx):

    larray = list(array[sIdx:mIdx])
    rarray = list(array[mIdx:eIdx])
    CLSR_logger.info("Merging\n{} \nwith\n{}".format(larray, rarray))

    larray.append(math.inf)
    rarray.append(math.inf)

    for i in range(sIdx, eIdx):
        if larray[0] <= rarray[0] or math.isinf(rarray[0]):
            array[i] = larray.pop(0)
        elif rarray[0] < larray[0] or math.isinf(larray[0]):
            array[i] = rarray.pop(0)

    CLSR_logger.info("Merged array is: %r" % str(array))
    return(array)

def partition(array, sIdx, eIdx):

    # Select random index and switch it with last index
    iIdx = random.randint(sIdx,eIdx)
    array[eIdx], array[iIdx] = array[iIdx], array[eIdx]

    
    x = array[eIdx]
    i = sIdx-1

    for j in range(sIdx, eIdx):
        if array[j] <= x:
            i+=1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[eIdx] = array[eIdx], array[i+1]
    return (i+1)

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False    

    return True
