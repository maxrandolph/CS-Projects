"""
File: testquicksort.py

Tests the quicksort algorithm
"""
import sys
import random

def quicksort(lyst):
    quicksortHelper(lyst, 0, len(lyst) - 1)
    

def quicksortHelper(lyst, left, right):
    if left < right:
        pivotLocation = partition(lyst, left, right)
        quicksortHelper(lyst, left, pivotLocation - 1)
        quicksortHelper(lyst, pivotLocation + 1, right)

def partition(lyst, left, right):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    # Exchange the pivot item and the boundary item
    swap (lyst, right, boundary)
    return boundary

def swap(lyst, i, j):
    """Exchanges the items at positions i and j."""
    # You could say lyst[i], lyst[j] = lyst[j], lyst[i]
    # but the following code shows what is really going on
    global swaps
    swaps+=1
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp
 





def main(size = 20, sort = quicksort):
    global swaps; swaps = 0
    count=0
    lyst = []
    fp = open(sys.argv[1], 'r')
    for line in fp:
        lyst.append(int(line))
        count+=1
    sort(lyst)
    print("Swaps:", swaps)
    print("Numbers:", count)

if __name__ == "__main__":
    main() 
