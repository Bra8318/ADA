def linear(arr,target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

arr = [10,25,35,41,68,25,19,37]
target = 45
result = linear(arr,target)

if (result != -1):
    print("Element found at index: ",result)
else:
    print("Element not found in the array")