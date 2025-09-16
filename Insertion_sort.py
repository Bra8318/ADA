def insertion(arr):
    for i in range(1,len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key


arr = [25,14,12,68,53,47,23]
insertion(arr)
for i in range(len(arr)):
    print(arr[i],end = ',')