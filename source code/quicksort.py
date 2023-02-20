import random
import time

# Python program for implementation of Quicksort Sort
# This implementation utilizes pivot as the last element in the nums list
  
def quicksort(l, r, arr):
    if len(arr) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
        return arr
    if l < r:
        pi = partition(l, r, arr)
        quicksort(l, pi-1, arr)  # Recursively sorting the left values
        quicksort(pi+1, r, arr)  # Recursively sorting the right values
    return arr 
 
def partition(l, r, nums):
    # Last element will be the pivot and the first element the pointer
    pivot = nums[r][4]
    ptr = l
    for i in range(l, r):
        if nums[i][4] <= pivot:
            # Swapping values smaller than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Finally swapping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr


# function to read text file and apply quick sort on sum column and print the output in another text file
def read_textFile(inputTextfile, outputFile):
    with open(inputTextfile, 'r') as f:
        readSumColumn = ([row.strip().split() for row in f])

    for x in range(0, len(readSumColumn)):
        readSumColumn[x] = list(map(int,readSumColumn[x]))

    start_time = time.time()
    array = quicksort(0, len(readSumColumn)-1, readSumColumn)
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
read_textFile('arr20.txt', 'arrQK_O_20.txt')
read_textFile('arr100.txt', 'arrQK_O_100.txt')
read_textFile('arr1000.txt', 'arrQK_O_1000.txt')
read_textFile('arr4000.txt', 'arrQK_O_4000.txt')