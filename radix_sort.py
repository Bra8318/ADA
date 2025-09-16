def count_sort_radix(arr,exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        index = (num // exp)% 10
        count[index] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    for num in reversed(arr):
        index = (num // exp)% 10
        output[count[index]-1] = num
        count[index] -= 1

    return output

def radix_sort(arr):
    if not arr:
        return arr
    
    max_value = max(arr)
    exp = 1
    while max_value // exp > 0:
        arr = count_sort_radix(arr,exp)
        exp *= 10
    return arr


arr = [25,14,12,68,53,47,23,25]
print(radix_sort(arr))
