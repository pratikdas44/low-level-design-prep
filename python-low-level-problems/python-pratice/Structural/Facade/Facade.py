from abc import ABC, abstractmethod

class Sorter:
    def sort(self):
        pass

class MergeSort(Sorter):
    def sort(self):
        print("Merge sort")


class BubbleSort(Sorter):
    def sort(self):
        print("Bubble sort")        

class SortingManager:
    def __init__(self, bubbleSort, mergeSort):
        self.bubbleSort = bubbleSort
        self.mergeSort = mergeSort

    def doBubbleSort(self):
        self.bubbleSort.sort()

    def doMergeSort(self):
        self.mergeSort.sort()

sortingManger = SortingManager()
sortingManger.doBubbleSort()