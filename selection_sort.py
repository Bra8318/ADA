def selection(arr):
    n = len(arr)
    for i in range(n):
        min_index = i

        for j in range(i+1,n):
           if arr[j] < arr[min_index]:
               min_index = j

        arr[i], arr[min_index] = arr[min_index],arr[i]
    return arr

arr = [25,14,12,68,53,47,23,25]
print(selection(arr))