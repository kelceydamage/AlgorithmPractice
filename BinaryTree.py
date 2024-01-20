from typing import BinaryIO


class HeapUtilities:

    @staticmethod
    def BuildMaxHeap(array, heapSize):
        """Convert an array into a max heap"""
        # Conduct an amount of loops equal to the floor of half the array length
        # to build the initial heap.
        for nodeIndex in range(heapSize // 2, -1, -1):
            HeapUtilities.NodeSort(array, heapSize, nodeIndex)
        print(f"Max heap built: {array}")

    @staticmethod
    def HeapSort(array):
        """ Sort an arbitrary array by converting it into a heap first.
        """
        heapSize = len(array)
    
        HeapUtilities.BuildMaxHeap(array, heapSize)
    
        for decrementedHeapSize in range(heapSize - 1, 0, -1):
            HeapUtilities.SwapNodePositions(array, decrementedHeapSize, 0)
            #print(f"step: {i} result: {array}")
            HeapUtilities.NodeSort(array, decrementedHeapSize, 0)
            #print(f"step: {i} result: {array}")

    @staticmethod
    def NodeSort(array, heapSize, nodeIndex):
        """Recursively sort the array as a balanced binary tree"""
        # Set the current largest value as the parent value.
        indexOfLargestValue = nodeIndex
        # Using the balanced binary tree principle of [K -1 / 2] parents and
        # 2K+1, 2K+2 for children where K == the current node, calculate the
        # current nodes childrens indices in the array.
        indexOfleftChild = 2 * nodeIndex + 1
        indexOfrightChild = 2 * nodeIndex + 2

        # Select left child as the largest value if the value of the current
        # position is less than the value of the left child. (and the left child 
        # is a valid element in the array)
        if indexOfleftChild < heapSize and array[indexOfLargestValue] < array[indexOfleftChild]:
            indexOfLargestValue = indexOfleftChild

        # Select right child as the largest value if the value of the current
        # largest position is less than the value of the right child. (and the 
        # right child is a valid element in the array)
        if indexOfrightChild < heapSize and array[indexOfLargestValue] < array[indexOfrightChild]:
            indexOfLargestValue = indexOfrightChild

        # If the results of the above cause an inequality between the current
        # largest value and the current parent value, swap position and recurse.
        if indexOfLargestValue != nodeIndex:
            HeapUtilities.SwapNodePositions(array, nodeIndex, indexOfLargestValue)
            HeapUtilities.NodeSort(array, heapSize, indexOfLargestValue)

    @staticmethod
    def SwapNodePositions(array, nodeIndex, indexOfLargestValue):
        """swap the positions of 2 nodes in an array"""
        array[nodeIndex], array[indexOfLargestValue] = array[indexOfLargestValue], array[nodeIndex]


class SearchUtilities:

    @staticmethod
    def BinarySearch(sortedArray, left, right, valueToFind):
        if (left > right):
            return -1
        midpoint = left + ((right - left)) // 2

        if sortedArray[midpoint] == valueToFind:
            return midpoint
        
        if sortedArray[midpoint] > valueToFind:
            return SearchUtilities.BinarySearch(sortedArray, left, midpoint -1, valueToFind)
        return SearchUtilities.BinarySearch(sortedArray, midpoint + 1, right, valueToFind)


if __name__ == "__main__":
    array = [1,12,9,5,6,10]
    print(f'Initial array: {array}')
    HeapUtilities.HeapSort(array)

    print(f'Sorted array: {array}')

    for value in array:
        indexOfValue = SearchUtilities.BinarySearch(array, 0, len(array), value)
        print(f"Search: {value}, found at index: {indexOfValue}")
