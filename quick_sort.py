def quick(arr):
    if len(arr)<= 1:
        return arr
    
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick(left) + [pivot] + quick(right)


#using iterative approach.
# def quick(arr):
#     if len(arr)<= 1:
#         return arr
    
#     stack = [(0, len(arr)-1)] # start and end indices.
#     while stack:
#         start,end = stack.pop()
#         if start >= end:
#             continue
#         pivot = partition(arr,start,end)
#         stack.append((start,pivot-1))
#         stack.append((pivot+1,end))
#     return arr

# def partition(arr,low,high):
#     pivot = arr[high]
#     i = low - 1
#     for j in range(low,high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i],arr[j] = arr[j],arr[i]

#     arr[i+1],arr[high] = arr[high],arr[i+1]
#     return i+1


arr = [25,14,12,68,53,47,23,25]
print(quick(arr))