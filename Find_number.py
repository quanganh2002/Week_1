def binary_search_first(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            high = mid - 1
            result = mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

def binary_search_last(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            low = mid + 1
            result = mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

def find_number(arr, target):
    return binary_search_first(arr, target), binary_search_last(arr, target)

nums = [5,6,7,8,8,8,8,10,12,15]
target = 8

print(find_number(nums, target))