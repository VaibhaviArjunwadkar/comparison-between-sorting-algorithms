import random
import time
readSumColumn = []

# function to generate arr20.txt file with 20 sets of rows
def create_arr20():
    sum20 = 0
    file20 = open('arr20.txt', 'w')
    for i in range(20):
        file20.write("%d "%(i+1))
        for j in range(3):
            y = random.randrange(1,99)
            sum20=sum20+y
            file20.write("%d "%y)
        file20.write("%d "%sum20)
        file20.write("\n")
        sum20 = 0   
    file20.close()

# function to generate arr100.txt file with 100 sets of rows
def create_arr100():
    sum100 = 0
    file100 = open('arr100.txt', 'w')
    for i in range(100):
        file100.write("%d "%(i+1))
        for j in range(3):
            y = random.randrange(1,99)
            sum100=sum100+y
            file100.write("%d "%y)
        file100.write("%d "%sum100)
        file100.write("\n")
        sum100 = 0   
    file100.close()

# function to generate arr1000.txt file with 1000 sets of rows
def create_arr1000():
    sum1000 = 0
    file1000 = open('arr1000.txt', 'w')
    for i in range(1000):
        file1000.write("%d "%(i+1))
        for j in range(3):
            y = random.randrange(1,99)
            sum1000=sum1000+y
            file1000.write("%d "%y)
        file1000.write("%d "%sum1000)
        file1000.write("\n")
        sum1000 = 0   
    file1000.close()

# function to generate arr4000.txt file with 4000 sets of rows
def create_arr4000():
    sum4000 = 0
    file4000 = open('arr4000.txt', 'w')
    for i in range(4000):
        file4000.write("%d "%(i+1))
        for j in range(3):
            y = random.randrange(1,99)
            sum4000=sum4000+y
            file4000.write("%d "%y)
        file4000.write("%d "%sum4000)
        file4000.write("\n")
        sum4000 = 0   
    file4000.close()


# calling above 4 functions which will create 4 seperate text files with 20, 100, 1000, 4000 sets respectively
create_arr20()
create_arr100()
create_arr1000()
create_arr4000()


# Function for insertion sort
def insertion_sort(arr):

        for ind in range(1, len(arr)):

            value = arr[ind]
            key = value[4]

            curInd = ind - 1
            valuei = arr[curInd]
            ikey = valuei[4]
            while curInd >= 0 and key < ikey:
                arr[curInd + 1] = valuei
                curInd -= 1
                valuei = arr[curInd]
                ikey = valuei[4]
            arr[curInd + 1] = value
        return arr


# function to read text file and apply insertion sort on sum column and print the output in another text file
def read_textFile(inputTextfile, outputFile):
    with open(inputTextfile, 'r') as f:
        readSumColumn = ([row.strip().split() for row in f])

    for x in range(0, len(readSumColumn)):
        readSumColumn[x] = list(map(int,readSumColumn[x]))

    start_time = time.time()
    array = insertion_sort(readSumColumn)
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
read_textFile('arr20.txt', 'arrIS_O_20.txt')
read_textFile('arr100.txt', 'arrIS_O_100.txt')
read_textFile('arr1000.txt', 'arrIS_O_1000.txt')
read_textFile('arr4000.txt', 'arrIS_O_4000.txt')

