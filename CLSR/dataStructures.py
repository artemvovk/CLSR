#!/usr/bin/env python
import math
from .helpers import CLSR_logger, merge

CLSR_logger.curMod(__name__)

class Heap():

    def __init__(self, nodes):
        self.nodes = nodes
        self.heapSize = len(nodes)
        self.heapType = None

    def __repr__(self):
        return str(self.nodes)

    def parent(self, i=0):
        if i < 1 or i >= self.heapSize:
            return None
        return (i-1) >> 1

    def leftChild(self, i=0):
        lIdx = ((i << 1)+1)
        if lIdx < self.heapSize:
            return lIdx
        return None
    
    def rightChild(self, i=0):
        rIdx = ((i << 1)+2)
        if rIdx < self.heapSize:
            return rIdx
        return None
        
    def maxHeapify(self, i=0):
        self.heapType = 'Max'
        l = self.leftChild(i)
        r = self.rightChild(i)

        if l and self.nodes[l] > self.nodes[i]:
            largest = l
        else:
            largest = i

        if r and self.nodes[r] > self.nodes[largest]:
            largest = r

        if largest != i:
            self.nodes[i], self.nodes[largest] = self.nodes[largest], self.nodes[i]
            self.maxHeapify(largest)

    def buildMaxHeap(self, fromNodes=[]):
        if fromNodes:
            self.nodes = fromNodes
            self.heapSize = len(fromNodes)
        for i in range(self.heapSize//2, -1, -1):
            self.maxHeapify(i)

    def minHeapify(self, i=0):
        self.heapType = 'Min'
        l = self.leftChild(i)
        r = self.rightChild(i)

        if l and self.nodes[l] < self.nodes[i]:
            smallest = l
        else:
            smallest = i

        if r and self.nodes[r] < self.nodes[smallest]:
            smallest = r

        if smallest != i:
            self.nodes[i], self.nodes[smallest] = self.nodes[smallest], self.nodes[i]
            self.minHeapify(smallest)

    def buildMinHeap(self, fromNodes=[]):
        if fromNodes:
            self.nodes = fromNodes
            self.heapSize = len(fromNodes)

        for i in range(self.heapSize//2, -1, -1):
            self.minHeapify(i)
    
    def heapMax(self):
        self.buildMaxHeap()
        return self.nodes[0]
    
    def heapMin(self):
        self.buildMinHeap()
        return self.nodes[0]

    def popMax(self):
        if self.heapSize == 1:
            return self.nodes.pop()

        self.buildMaxHeap()
        self.nodes[0], self.nodes[self.heapSize-1] = self.nodes[self.heapSize-1], self.nodes[0]
        self.heapSize -= 1

        heapMax = self.nodes.pop(self.heapSize)
        self.maxHeapify()
        return heapMax
    
    def popMin(self):
        if self.heapSize == 1:
            return self.nodes.pop()

        self.buildMinHeap()
        self.nodes[0], self.nodes[self.heapSize-1] = self.nodes[self.heapSize-1], self.nodes[0]
        self.heapSize -= 1

        heapMin = self.nodes.pop(self.heapSize)
        self.minHeapify()
        return heapMin

    def changeKey(self, i, newValue):
        if self.heapType == 'Min':
            self.nodes[i] = newValue
            while i and self.nodes[self.parent(i)] > self.nodes[i]:
                self.nodes[i], self.nodes[self.parent(i)] = self.nodes[self.parent(i)], self.nodes[i]
                i = self.parent(i)

        else:
            self.nodes[i] = newValue
            while i and self.nodes[self.parent(i)] < self.nodes[i]:
                self.nodes[i], self.nodes[self.parent(i)] = self.nodes[self.parent(i)], self.nodes[i]
                i = self.parent(i)

    def insertKey(self, newValue):
        if self.heapType == 'Min':
            self.heapSize += 1
            self.nodes.append(math.inf)
            self.changeKey(self.heapSize-1, newValue)
        else:
            self.heapSize += 1
            self.nodes.append(-math.inf)
            self.changeKey(self.heapSize-1, newValue)


    def deleteNode(self, index):
        if self.heapType == 'Min':
            self.heapSize -= 1
            self.nodes.pop(index)
            self.minHeapify(index-1)
        else:
            self.heapSize -= 1
            self.nodes.pop(index)
            self.maxHeapify(index-1)
            
