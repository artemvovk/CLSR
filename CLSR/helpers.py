#!/usr/bin/env python

import logging, math, random

# Setting up logger for good output
LOG_FORMAT = '\n==%(asctime)s in %(module)s:==\n%(message)s\n'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
CLSR_logger = logging.getLogger(__file__)


# Random Array Generators:

rand_array_100_pos = [50]
rand_array_100_pos.extend([int(1000*random.random()) for i in range(99)])

rand_array_100_neg = [-50]
rand_array_100_neg.extend([int(1000*random.uniform(0,-1)) for i in range(99)])

rand_array_100_both = [-50]
rand_array_100_both.extend([int(1000*random.uniform(1,-1)) for i in range(99)])

rand_array_100_count = [int(100*random.random()) for i in range(100)]

rand_array_100_weighted = list()
weights = [int(100*random.random()) for i in range(100)]
for i in rand_array_100_count:
    for j in weights:
        rand_array_100_weighted.append((rand_array_100_count[i], weights[j]))

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
