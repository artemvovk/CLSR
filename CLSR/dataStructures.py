#!/usr/bin/env python

from helpers import CLSR_logger, merge

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

