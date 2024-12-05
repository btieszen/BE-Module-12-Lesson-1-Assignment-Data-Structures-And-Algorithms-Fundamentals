def simple_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return(arr)
my_arr=[75,12,34,43,25,67,54,65,30,98]
print(simple_sort(my_arr))