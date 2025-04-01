# Examples
arr1 = [4, 5, 2, 3, 1]
arr2 = [89, 45, 68, 90, 29, 34, 17]

# Implementations of Selection sort

def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # TODO: write quick swap function maybe
        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp

# Examples tested
print(arr1)
selection_sort(arr1)
print(arr1)

print(arr2)
selection_sort(arr2)
print(arr2)