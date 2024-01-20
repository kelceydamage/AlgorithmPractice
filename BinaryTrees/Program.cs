namespace MySorting 
{
    public class HeapUtilities
    {
        public static void BuildMaxHeap(int[] inputArray, int heapSize)
        {
            for (int nodeIndex = (heapSize) / 2; nodeIndex >= 0; nodeIndex--)
            {
                NodeSort(inputArray, heapSize, nodeIndex);
            }
            Console.WriteLine($"Max heap build: {string.Join(",", inputArray)}");
        }

        public static void HeapSort(int[] inputArray)
        {
            int heapSize = inputArray.Length;
            BuildMaxHeap(inputArray, heapSize);
            
            for (int decrementedHeapSize = heapSize - 1; decrementedHeapSize >= 0; decrementedHeapSize--)
            {
                SwapNodePositions(inputArray, decrementedHeapSize, 0);
                NodeSort(inputArray, decrementedHeapSize, 0);
            }
        }

        private static void NodeSort(int[] inputArray, int heapSize, int nodeIndex)
        {
            int indexOfLargestValue = nodeIndex;
            int indexOfleftChild = 2 * nodeIndex + 1;
            int indexOfrightChild = 2 * nodeIndex + 2;

            if (indexOfleftChild < heapSize && inputArray[indexOfLargestValue] < inputArray[indexOfleftChild])
            {
                indexOfLargestValue = indexOfleftChild;
            }

            if (indexOfrightChild < heapSize && inputArray[indexOfLargestValue] < inputArray[indexOfrightChild])
            {
                indexOfLargestValue = indexOfrightChild;
            }
            if (indexOfLargestValue != nodeIndex)
            {
                SwapNodePositions(inputArray, nodeIndex, indexOfLargestValue);
                NodeSort(inputArray, heapSize, indexOfLargestValue);
            }
        }

        private static void SwapNodePositions(int[] inputArray, int nodeIndex, int indexOfLargestValue)
        {
            int temp = inputArray[nodeIndex];
            inputArray[nodeIndex] = inputArray[indexOfLargestValue];
            inputArray[indexOfLargestValue] = temp;
        }
    }

    class SearchUtilities
    {
        public static int BinarySearch(int[] sortedArray, int leftIndex, int rightIndex, int valueToFind)
        {
            if (leftIndex > rightIndex) return -1;
            int midpoint = leftIndex + (rightIndex - leftIndex) / 2;

            if (sortedArray[midpoint] == valueToFind) return midpoint;

            if (sortedArray[midpoint] > valueToFind) return BinarySearch(sortedArray, leftIndex, midpoint - 1, valueToFind);

            return BinarySearch(sortedArray, midpoint + 1, rightIndex, valueToFind);
        }
    }

    class Program
    {
        public static void Main()
        {
            int[] inputArray = new int[6] {1,12,9,5,6,10};
            Console.WriteLine($"Initial array: {string.Join(",", inputArray)}");
            HeapUtilities.HeapSort(inputArray);
            Console.WriteLine($"Sorted array: {string.Join(",", inputArray)}");

            foreach (int value in inputArray)
            {
                int indexOfValue = SearchUtilities.BinarySearch(inputArray, 0, inputArray.Length, value);
                Console.WriteLine($"Search: {value}, found at index: {indexOfValue}");
            }
        }
    }
}
