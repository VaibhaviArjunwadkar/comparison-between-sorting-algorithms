import random
import time

# Function for merge
def mergeSort(arr, left, right):
    if left >= right:
        return

    middle = (left + right)//2
    mergeSort(arr, left, middle)
    mergeSort(arr, middle + 1, right)
    merge(arr, left, middle, right)
    return arr


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i][4] <= R[j][4]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there  are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
   

# function to read text file and apply merge sort on sum column and print the output in another text file
def read_textFile(inputTextfile, outputFile):
    with open(inputTextfile, 'r') as f:
        readSumColumn = ([row.strip().split() for row in f])

    for x in range(0, len(readSumColumn)):
        readSumColumn[x] = list(map(int,readSumColumn[x]))

    start_time = time.time()
    array = mergeSort(readSumColumn, 0, len(readSumColumn) -1)
    end_time = time.time()

    for u in range(len(array)):
        value = array[u]
        value[0] = u+1

    for x in range(0, len(array)):
        array[x] = list(map(str,array[x]))


    with open(outputFile, 'w') as txt_file:
        for line in array:
            txt_file.write(" ".join(line)+"\n")

    time_taken = end_time - start_time
    file_object = open(outputFile, 'a')
    file_object.write("\nSorting complete. Time taken: %f seconds" %time_taken)
    # Close the file
    file_object.close()


# calling read_textFile function
read_textFile('arr20.txt', 'arrMR_O_20.txt')
read_textFile('arr100.txt', 'arrMR_O_100.txt')
read_textFile('arr1000.txt', 'arrMR_O_1000.txt')
read_textFile('arr4000.txt', 'arrMR_O_4000.txt')