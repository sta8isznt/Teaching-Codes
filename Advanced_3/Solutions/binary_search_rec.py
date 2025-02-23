def binary_search(arr, left, right, target):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)

arr = [1, 3, 5, 7, 9, 11]
target = int(input("Enter the number"))
index = binary_search(arr, 0, len(arr) - 1, target)
print(f"The number {target} found in {index} position" if index != -1 else "The number is not in the list")
