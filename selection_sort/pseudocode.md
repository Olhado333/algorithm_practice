# Pseudocode for selection sort

## First implementation

Notes:
- Function mutates input data. May write implementation without this downside.

ALGORITHM SelectionSort(A[0..n-1])\
    //Sorts a given array by selection sort\
    //Input: An array A[0..n-1] of orderable elements\
    //Output: Array A[0..n-1] sorted in nondecreasing orderable\
    for i <- 0 to n - 2 do\
        min <- i\
        for j <- i + 1 to n - 1 do\
            if A[j] < A[min]\
                min <- j\
        swap A[i] and A[min]\
