from pytest import *

import sys
sys.path.insert(0, "~/Dropbox/Coding/python/src/github.com/kierachell/CLSR")
from CLSR import sorts, helpers

@fixture
def pos_dummies():
    return [dummy for dummy in [helpers.getRandomArray(i, 10*i) for i in [10**n for n in range(1,5)] ]]


def teardown():
    print ("TEAR DOWN!")

def test_quicksort(pos_dummies):
    assert [sorted(dummy) == sorts.quicksort(dummy) for dummy in pos_dummies]

def test_insertionSort(pos_dummies):
    assert [sorted(dummy) == sorts.insertionSort(dummy) for dummy in pos_dummies]
    
def test_selectionSort(pos_dummies):
    assert [sorted(dummy) == sorts.selectionSort(dummy) for dummy in pos_dummies]

def test_bubbleSort(pos_dummies):
    assert [sorted(dummy) == sorts.bubbleSort(dummy) for dummy in pos_dummies]

def test_heapSort(pos_dummies):
    assert [sorted(dummy) == sorts.heapSort(dummy) for dummy in pos_dummies]

def test_mergeSort(pos_dummies):
    assert [sorted(dummy) == sorts.mergeSort(dummy) for dummy in pos_dummies]

def test_radixSort(pos_dummies):
    assert [sorted(dummy) == sorts.radixSort(dummy) for dummy in pos_dummies]
