#!/usr/bin/env python
import math, random
from .helpers import *

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
            

class Stack():
    def __init__(self, size):
        self.items = [None]*size
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def push(self, item):
        if self.top == len(self.items)-1:
            return False
        self.top += 1
        self.items[self.top] = item
        return True

    def pop(self):
        if self.isEmpty():
            return False
        else:
            x = self.items[self.top]
            self.items[self.top] = None
            self.top -= 1
            return x

class Queue():
    def __init__(self, size):
        self.items = [None]*size
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        if self.tail == len(self.items):
            self.tail = 0
        if self.items[self.tail]:
            return False
        self.items[self.tail] = item
        self.tail+=1
        return True

    def dequeue(self):
        if not self.items[self.head]:
            return False
        item = self.items[self.head]
        self.items[self.head] = None
        if self.head == len(self.items)-1:
            self.head = 0
        else:
            self.head += 1
        return item

class LLHead():
    def __init__(self, val):
        self.val = val
        self.ne = None
        self.pr = None

    def listSearch(self, key):
        x = self.key
        while x and self.key != key:
            x = self.ne
        return x

    def listInsert(self, val):
        x = LLHead(val)
        x.ne = self
        self.pr = x

    def listDelete(self, key):
        x = self.listSearch(key)
        if x.pr:
            x.pr.ne = x.ne
        else:
            self = x.ne
        if x.ne:
            x.ne.pr = x.pr

class HashTable():
    def __init__(self, size, hashtype = "unihash", probeType = "doublehash"):
        self.table = [None]*size
        self.mod = size
        self.hashf = self.makeHahsFunc(hashtype)
        self.probe = self.makeProbeFunc(probeType)

    def makeHahsFunc(self, hashtype = "unihash"):
        if hashtype == "multiply":
            A = random.uniform(0,1)
            return lambda x: math.floor(self.mod*(x*A-math.floor(x*A)))
        elif hashtype == "divide":
            return lambda x: x%self.mod
        elif hashtype == "unihash":
            primes = [i for i in range(self.mod-1, 2**self.mod) if isPrime(i)]
            p = random.choice(primes)
            a = random.randint(1, p)
            b = random.randint(0,p-1)
            return lambda x: ((a*x+b)%p)%self.mod
        return lambda x: x%self.mod

    def makeProbeFunc(self, probeType = "doublehash"):
        if probeType == "linear":
            return lambda key, i: (self.hashf(key)+i) % self.mod
        elif probeType == "quadratic":
            quadProbeConst = (random.randint(0,self.mod), random.randint(1, self.mod-1))
            return lambda key, i: (self.hashf(key)+quadProbeConst[0]*i+quadProbeConst[1]*i*i)%self.mod
        elif probeType == "doublehash":
            return lambda key, i: (self.hashf(key) + i*self.hashf(key))%self.mod
        return lambda key, i: (key+i)%self.mod

    def insert(self, key):
        loc = self.hashf(key)
        if not self.table[loc]:
            self.table[loc] = key
            return True
        elif type(self.table[loc]) == list:
            self.table[loc].append(key)
            return True
        else:
            self.table[loc] = [key, self.table[loc]]
            return True

class Node():
    def __init__(self, key, val, par = None, left = None, right = None):
        self.key = key
        self.val = val
        self.par = par
        self.left = left
        self.right = right
        
class BST():
    def __init__(self, root):
        self.root = root

    def inOrderTreeWalk(self, node):
        if node != None:
            self.inOrderTreeWalk(node.left)
            print(node.key)
            self.inOrderTreeWalk(node.right)

    def inOrderTreeWalkIter(self, node):
        sStack = [node]
        cur = node
        while cur.left:
            cur = cur.left
            sStack.append(cur)
        while sStack:
            cur = sStack.pop()
            print(cur.key)
            if cur.right:
                cur = cur.right
                while cur.left:
                    sStack.append(cur.left)
                    cur = cur.left

    def treeSearch(self, key, node = None):
        if not node:
            node = self.root
        if key == None or key == node.key:
            return node
        if k < node.key:
            return self.treeSearch(key, node.left)
        else:
            return self.treeSearch(key, node.right)

    def treeSearchIter(self, key, node = None):
        if not node:
            node = self.root
        while node and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node

    def treeMin(self, node = None):
        if not node:
            node = self.root
        while node.left:
            node = node.left
        return node
                
    def treeMax(self, node = None):
        if not node:
            node = self.root
        while node.right:
            node = node.right
        return node

    def treeSucc(self, node = None):
        if not node:
            node = self.root
        if node.right:
            return self.treeMin(node.right)
        succ = node.parent
        while y and node == succ.right:
            node = succ
            succ = succ.par
        return succ

    def treePred(self, node = None):
        if not node:
            node = self.root
        if node.left:
            return self.treeMax(node.left)
        pred = node.parent
        while y and node == pred.left:
            node = pred
            pred = pred.par
        return pred

    def treeInsert(self, node):
        pred = None
        cur = self.root
        while cur:
            pred = cur
            if node.key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        node.par = pred
        if not pred:
            self.root = node
        elif node.key < pred.key:
            pred.left = node
        else:
            pred.right = node

    def transplant(self, dest, node):
        if not dest.par:
            self.root = node
        elif dest == dest.par.left:
            dest.par.left = node
        else:
            dest.par.right = node
        if node:
            node.par = dest.par

    def treeDelete(self, node):
        if not node.left:
            self.transplant(node, node.right)
        elif not node.right:
            self.transplant(node, node.left)
        else:
            cur = self.treeMin(node.right)
            if cur.par != node:
                self.transplant(cur, cur.right)
                cur.right = node.right
                cur.right.par = cur
            self.transplant(node, cur)
            cur.left = node.left
            cur.left.par = cur
