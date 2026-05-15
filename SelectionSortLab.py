# Implement the Selection Sort Algorithm

def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element        
        if(min_idx != i):
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

# Example usage
data = [33, 1, 89, 2, 67, 245]
sorted_data = selection_sort(data)
print(f"Sorted array: {sorted_data}")