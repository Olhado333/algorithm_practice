# Examples
arr1 = [5, 3, 4, 2, 1]
arr2 = [89, 45, 68, 90, 29, 34, 17]

# Implementations
def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j + 1] < arr[j]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

# Examples tested
print(arr1)
bubble_sort(arr1)
print(arr1)

print(arr2)
bubble_sort(arr2)
print(arr2)