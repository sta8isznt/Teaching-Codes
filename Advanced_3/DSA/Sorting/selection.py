def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        # Check the rest of the array for a smaller element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Step {i + 1}: {arr}")

# Example usage
array = [64, 34, 25, 12, 22, 11, 90]
selection_sort(array)
print("Sorted array:", array)
