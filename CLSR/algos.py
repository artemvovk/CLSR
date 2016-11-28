import os, sys, math, random  

def linearSearch(array, num):
    print("Searching for %r" % num)
    for j in range(0, len(array)-1):
        if array[j] == num:
            print("Found %r at index %r" % (array[j], j))
            return
    print("Not found")
  
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

def mergeSort(array):
    if len(array) > 1:
        midl = math.ceil(len(array)/2)
        larray = mergeSort(list(array[:midl]))
        rarray = mergeSort(list(array[midl:]))
        tarray = larray + rarray
        #print("Sorted array is: %r" % str(tarray))
        return merge(tarray)
    return array
        


def getMaxCrossSubarray(array):
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
    #print("We got max crossing subarray at %r to %r with sum of %r" % (mleft, mright, lsum+rsum))
    return lsum+rsum

def getMaxSubarray(array):
    if len(array) == 1:
        return array[0]
    else:
        midl = math.ceil(len(array)/2)
        lsum = getMaxSubarray(array[:midl])
        rsum = getMaxSubarray(array[midl:])
        msum = getMaxCrossSubarray(array)

        if lsum >= rsum and lsum >= msum:
            print("We got left sum at %r" % (lsum))
            return lsum
        elif rsum >= lsum and rsum >= msum:
            print("We got right sum at %r" % (rsum))
            return rsum
        else:
            print("We got mid sum at %r" % (msum))
            return msum

def randomInPlace(array):
    n = len(array)
    for i in range(0,n):
        randIdx = int((n-i)*random.random())
        array[i], array[randIdx] = array[randIdx], array[i]
    print("We randomized the array at %r" % str(array))

def MarceauRandomInPlace(array):
    n = len(array)
    randIdx = int((n-0)*random.random())
    array[0], array[randIdx] = array[randIdx], array[0]
    for i in range(0,n):
        randIdx = int((n-i)*random.random())
        array[i], array[randIdx] = array[randIdx], array[i]
    print("Marceau randomized the array at %r" % str(array))

def KelpRandomInPlace(array):
    n = len(array)-1
    for i in range(0,n):
        randIdx = int((n-i)*random.random())
        array[i], array[randIdx] = array[randIdx], array[i+1]
    print("Kelp randomized the array at %r" % str(array))

def randomWithAll(array):
    n = len(array)
    for i in range(0,n):
        randIdx = int((n)*random.random())
        array[i], array[randIdx] = array[randIdx], array[i]
    print("We randomized the array with all at %r" % str(array))

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
    print("We randomized the array at %r" % str(array))

def randomSearch(array, find):
    n = len(array)
    barray = list()
    i = random.randrange(0,n)
    steps = 0

    while array[i] != find:
        
        i = random.randrange(0,n)
        steps += 1
        if len(barray) == len(array) or steps == n*n:
            print("Didn't find %r in the array in %r steps" % (find, steps))
            return -1

        if array[i] not in barray:
            #print("Length of one is %r and length of other is %r" % (len(array), len(barray)))
            barray.append(array[i])
            
        
    print("Found %r at %r" % (find, i))
    return i

def deterministicSearch(array, find):
    n = len(array)
    for i in range(0,n):
        if array[i] == find:
            print("Found %r at %r" % (find, i))
            return i
    print("Didn't find %r in %r" % (find, array))
    return -1

class Node():
    
    def __init__(self, val, parent=None, lchild=None, rchild=None ):
        self.val = val
        self.parent=parent
        self.lchild = lchild
        self.rchild = rchild

    def __eq__(self, other):
        return self.val == other.val

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __le__(self, other):
        return self.val <= other.val

    def __ge__(self, other):
        return self.val >= other.val
    
    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

class Heap():

    def __init__(self, root, nodes=list()):
        self.nodes = nodes
        self.nodes.insert(0, root)
        self.nodify()

    def nodify(self):
        heapSize = len(self.nodes)
        for i in range(0, len(self.nodes)):
            self.nodes[i] = Node(val = self.nodes[i])
        if heapSize > 0:
            self.nodes[0].lchild = self.nodes[1]
            self.nodes[1].parent = self.nodes[0]
        if heapSize > 1:
            self.nodes[0].rchild = self.nodes[2]
            self.nodes[2].parent = self.nodes[0]

        for j in range(1, heapSize):
            if ((j*2)+1) < heapSize:
                self.nodes[j].lchild = self.nodes[(j*2)+1]
                self.nodes[(j*2)+1].parent = self.nodes[j]
            if ((j+1)*2) < heapSize:
                self.nodes[j].rchild = self.nodes[(j+1)*2]
                self.nodes[(j+1)*2].parent = self.nodes[j]
        #self.__repr__()

    def __repr__(self):
        for i in range(0, len(self.nodes)):
            print("Node at %r with vaue %r | lchild %r and rchild %r and parent %r" % (i, self.nodes[i],
                                                                                       self.nodes[i].lchild,
                                                                                       self.nodes[i].rchild,
                                                                                       self.nodes[i].parent))

        
    def maxHeapify(self, i=0):
        cur = self.nodes[i]
        largest = self.nodes[i]
        largeIdx = i
        if cur.lchild and cur.lchild > cur:
            largeIdx = self.nodes.index(cur.lchild)
            largest = cur.lchild            
        else:
            largeIdx = self.nodes.index(cur)
            largest = cur

        if cur.rchild and cur.rchild > largest:
            largeIdx = self.nodes.index(cur.rchild)
            largest = cur.rchild
            
        if i != largeIdx:
            self.nodes[largeIdx].val, self.nodes[i].val = cur.val, largest.val
            self.maxHeapify(largeIdx)

    def minHeapify(self, i=0):
        cur = self.nodes[i]
        minnest = self.nodes[i]
        minIdx = i
        if cur.lchild and cur.lchild < cur:
            minIdx = self.nodes.index(cur.lchild)
            minnest = cur.lchild            
        else:
            minIdx = self.nodes.index(cur)
            minnest = cur

        if cur.rchild and cur.rchild < minnest:
            minIdx = self.nodes.index(cur.rchild)
            minnest = cur.rchild
            
        if i != minIdx:
            self.nodes[minIdx].val, self.nodes[i].val = cur.val, minnest.val
            self.maxHeapify(minIdx)

    def heapMax(self):
        return self.nodes[0]

    def heapGetMax(self):
        heapSize = len(self.nodes)
        if heapSize == 0:
            return -1
        heapMax = self.nodes[0].val
        self.nodes[0].val = self.nodes[heapSize-1].val
        self.nodes.pop(heapSize-1)
        self.maxHeapify(0)
        return heapMax

    def increaseNode(self, index, newValue):
        if newValue < self.nodes[index].val:
            return -1
        self.nodes[index].val = newValue
        print("Parent of %r is %r" % (self.nodes[index], self.nodes[index].parent))
        while index > 0 and self.nodes[index].parent < self.nodes[index]:
            self.nodes[index].parent.val, self.nodes[index].val = self.nodes[index].val, self.nodes[index].parent.val
            index = self.nodes.index(self.nodes[index].parent)
        return index

    def maxHeapInsert(self, newValue):
        newNode = Node(val = -1 , parent = self.nodes[len(self.nodes)-1])
        self.nodes[-1].lchild = newNode
        self.nodes.append(newNode)
        return self.increaseNode(len(self.nodes)-1, newValue)

    def deleteNode(self, index):
        print("Deleting node %r" % self.nodes[index])
        self.nodes[index].val = -1000
        self.maxHeapify(index)
        for i in range(0, len(self.nodes)-1):
            if self.nodes[i].val == -1000:

                if self.nodes[i].parent.lchild.val == -1000:
                    self.nodes[i].parent.lchild = None
                    if self.nodes[i].parent.rchild:
                        self.nodes[i].parent.lchild = self.nodes[i].parent.rchild
                        self.nodes[i].parent.rchild = None
                else:
                    self.nodes[i].parent.rchild = None
                self.nodes.pop(i)

def qsPartition(array, sIdx, eIdx):
    
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

def quicksort(array):
    sIdx = 0
    eIdx = len(array)-1
    mIdx = qsPartition(array, sIdx, eIdx)
    subStack = [sIdx, mIdx, eIdx]
    
    while(len(subStack)>1):
        eIdx = subStack.pop()
        sIdx = subStack.pop()
        if sIdx+2 < eIdx and mIdx != qsPartition(array, sIdx, eIdx):
            mIdx = qsPartition(array, sIdx, eIdx)
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
    pivot = qsPartition(array, sIdx, eIdx)
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
        sum += item[1]
    return warray
    
    
    
            
#bubbleSort(dummyarray)
#merge(dummyarray)
#insertionSortAsc(dummyarray)
#insertionSortDesc(dummyarray)
#selectionSort(dummyarray)
#getMaxSubarray(dummynegarray)

#linearSearch(dummyarray, int(1000*random.random()))

#randomInPlace(dummyarray)
#MarceauRandomInPlace(dummyarray)
#KelpRandomInPlace(dummyarray)
#randomWithAll(dummyarray)
#randomByCyclic(dummyarray)
#randomSearch(dummyarray, 500)
#deterministicSearch(dummyarray, 500)



#mHeap = Heap(dummyarray[0], dummyarray[1:])
#for i in range(int(len(mHeap.nodes)/2+1),-1,-1):
#    mHeap.maxHeapify(i)


#mHeap.__repr__()

#print("Increasing value at %r" % mHeap.increaseNode(90, 500))
#print("Inserting new value at %r" % mHeap.maxHeapInsert(999))
#mHeap.deleteNode(10)
#mHeap.__repr__()

#quicksort(dummyarray)
#print("Partitioned dummy %r" % dummyarray)

#print("Counted array %r" % countingSort(countingarray, 100))


#MinMax = findMinMax(dummyarray)
#print("We got a min %r and max %r from that shit" % (MinMax[0], MinMax[1]))

#print("Sorted array is %r" % selectionSort(dummyarray))
#print("We got this from randomized select %r" % (randomizedSelect(dummyarray, 0, 99, 2)))

#print("Dummy array is: %r" % str(weightedarray))
#print("Sorted weighted array is %r" % str(weightedMedian(weightedarray)))


#-----------------------------------------------------#
#--------------------DATA STRUCTURES------------------#
#-----------------------------------------------------#

