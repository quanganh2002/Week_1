def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

def intersection(arr1, arr2):
    itst = []
    for i in arr1:
        if binary_search(arr2, i):
            itst.append(i)
    return itst

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7, 8]

print(intersection(arr1, arr2))