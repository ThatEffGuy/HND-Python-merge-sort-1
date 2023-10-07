import time
import random
from random import randint

def GenerateRandomNumbers():
    random_list = []
    howmany = int(input("How many numbers do you want to have in the list? "))
    for i in range(0, howmany):
        random_list.append(random.randint(0, 5000))
    return random_list


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = GenerateRandomNumbers()
mergeSort(myList)
theTime = str(time.perf_counter())
print("\n The sorted list: ", myList, " \n And the time taken: ", theTime)