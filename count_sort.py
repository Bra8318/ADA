def count_sort(arr):
    max_value = max(arr)
    n = len(arr)
    count = [0] * (max_value + 1)
    
    for num in arr:
        count[num] += 1

    for i in range(1,len(count)):
        count[i] += count[i-1]
    
    output = [0] * n
    for num in reversed(arr):
        output[count[num]-1] = num
        count[num] -= 1
    return output


arr = [25,14,12,68,53,47,23,25]
print(count_sort(arr))