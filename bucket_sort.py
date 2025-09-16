def bucket_sort(arr):
    n = len(arr)
    if n == 0:
        return arr
    
    bucket = [[] for _ in range(n)]
    for num in arr:
        index = int(num *n)
        bucket[index].append(num)

    sort = []
    for i in bucket:
        sort.extend(sorted(i))

    return sort

arr = [0.25,0.23,0.68,0.16,0.95,0.56,0.30]
print(bucket_sort(arr))