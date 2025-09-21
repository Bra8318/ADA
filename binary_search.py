def binary(arr,target):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid + 1
    return -1


arr = [10,25,35,41,68,25,19,37]
target = 41
result = binary(arr,target)

if (result != -1):
    print("Element found at index: ",result)
else:
    print("Element not found in the array")