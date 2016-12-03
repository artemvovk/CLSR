#!/usr/bin/env python
import random
from helpers import CLSR_logger

CLSR_logger.curMod(__name__)

def randomInPlace(array):
    n = len(array)
    for i in range(0,n):
        randIdx = random.randint(i, n)
        array[i], array[randIdx] = array[randIdx], array[i]
    CLSR_logger.info("We randomized the array at %r" % str(array))
    return array

def MarceauRandomInPlace(array):
    n = len(array)
    randIdx = random.randint(0,n)
    array[0], array[randIdx] = array[randIdx], array[0]
    for i in range(0,n):
        randIdx = random.randint(i,n)
        array[i], array[randIdx] = array[randIdx], array[i]
    CLSR_logger.info("Marceau randomized the array at %r" % str(array))
    return array

def KelpRandomInPlace(array):
    n = len(array)-1
    for i in range(0,n):
        randIdx = random.randint(i,n)
        array[i], array[randIdx] = array[randIdx], array[i+1]
    CLSR_logger.info("Kelp randomized the array at %r" % str(array))
    return array

def randomWithAll(array):
    n = len(array)
    for i in range(0,n):
        randIdx = random.randint(0,n)
        array[i], array[randIdx] = array[randIdx], array[i]
    CLSR_logger.info("We randomized the array with all at %r" % str(array))
    return array

def randomByCyclic(array):
    n = len(array)
    barray = [None]*n
    offset = int((n)*random.random())
    for i in range(0,n-1):
        dest = i+offset
        if dest > n-1:
            dest = dest-n
        barray[dest] = array[i]
    array = barray
    CLSR_logger.info("We randomized the array at %r" % str(array))
    return array
