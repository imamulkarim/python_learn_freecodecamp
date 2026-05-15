# Implement the Quicksort Algorithm

def quick_sort(inputNumbers):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(inputNumbers) <= 1:
        return inputNumbers
    
    # Selecting the middle element as the pivot
    pivot = inputNumbers[len(inputNumbers) // 2]
    
    # Partitioning the array
    left = [x for x in inputNumbers if x < pivot]
    middle = [x for x in inputNumbers if x == pivot]
    right = [x for x in inputNumbers if x > pivot]
    
    # Recursively sort and combine
    return quick_sort(left) + middle + quick_sort(right)


data = [3, 6, 8, 10, 1, 2, 1]
print(quick_sort(data)) # Output: [1, 1, 2, 3, 6, 8, 10]