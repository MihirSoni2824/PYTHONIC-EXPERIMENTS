def bubble_sort(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)

print("Sorted array is: ")

for i in range(len(arr)):
    print(arr[i])