def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) //2
    right = merge_sort(arr[mid:])
    left = merge_sort(arr[:mid])

    return merge(left,right)

def merge(left,right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


arr = [25,14,12,68,53,47,23,25]
print(merge_sort(arr))


