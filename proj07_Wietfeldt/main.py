# Project No.: 7
# Author: Tobyn Wietfeldt
# Description: Time complexity for sorting algorithms

# Importing for random numbers, time measurement, and recursion limit
import time
import random
import sys

# Preventing a recursion error
sys.setrecursionlimit(5002)


# Function for recursive insertion sorting algorithm
def insertionSort(arr, n):
    if n <= 1:
        return
    insertionSort(arr, n - 1)
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j + 1] = last


# Function for dividing list (used in quick sort)
def divide(array, low, high):
    split = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= split:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


# Function for recursive quick sorting algorithm
def quickSort(array, low, high):
    if low < high:
        div = divide(array, low, high)
        quickSort(array, low, div - 1)
        quickSort(array, div + 1, high)


# Function for recursive bubble sorting algorithm
def bubbleSort(arr, n=None):
    if n is None:
        n = len(arr)
    count = 0
    if n == 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            count = count + 1
    if count == 0:
        return
    bubbleSort(arr, n - 1)


# Creating lists with specified random integers and list lengths
list10 = [random.randint(1, 10) for i in range(10)]
list50 = [random.randint(1, 50) for j in range(50)]
list100 = [random.randint(1, 100) for k in range(100)]
list500 = [random.randint(1, 500) for r in range(500)]
list1000 = [random.randint(1, 1000) for m in range(1000)]
list5000 = [random.randint(1, 5000) for n in range(5000)]

# Running functions using shallow copies of generated lists
# Measuring time for computation
# Printing output for bubble, insertion and quick sort functions
print("Bubble Sort Times:")
start = time.time()
bubbleSort(list10[:], len(list10))
end = time.time()
print(f"    N = 10: {end - start} seconds")
start = time.time()
bubbleSort(list50[:], len(list50))
end = time.time()
print(f"    N = 50: {end - start} seconds")
start = time.time()
bubbleSort(list100[:], len(list100))
end = time.time()
print(f"    N = 100: {end - start} seconds")
start = time.time()
bubbleSort(list500[:], len(list500))
end = time.time()
print(f"    N = 500: {end - start} seconds")
start = time.time()
bubbleSort(list1000[:], len(list1000))
end = time.time()
print(f"    N = 1000: {end - start} seconds")
start = time.time()
bubbleSort(list5000[:], len(list5000))
end = time.time()
print(f"    N = 5000: {end - start} seconds")

print("Insertion Sort Times:")
start = time.time()
insertionSort(list10[:], len(list10))
end = time.time()
print(f"    N = 10: {end - start} seconds")
start = time.time()
insertionSort(list50[:], len(list50))
end = time.time()
print(f"    N = 50: {end - start} seconds")
start = time.time()
insertionSort(list100[:], len(list100))
end = time.time()
print(f"    N = 100: {end - start} seconds")
start = time.time()
insertionSort(list500[:], len(list500))
end = time.time()
print(f"    N = 500: {end - start} seconds")
start = time.time()
insertionSort(list1000[:], len(list1000))
end = time.time()
print(f"    N = 1000: {end - start} seconds")
start = time.time()
insertionSort(list5000[:], len(list5000))
end = time.time()
print(f"    N = 5000: {end - start} seconds")

print("Quick Sort Times:")
start = time.time()
quickSort(list10[:], 0, len(list10)-1)
end = time.time()
print(f"    N = 10: {end - start} seconds")
start = time.time()
quickSort(list50[:], 0, len(list50)-1)
end = time.time()
print(f"    N = 50: {end - start} seconds")
start = time.time()
quickSort(list100[:], 0, len(list100)-1)
end = time.time()
print(f"    N = 100: {end - start} seconds")
start = time.time()
quickSort(list500[:], 0, len(list500)-1)
end = time.time()
print(f"    N = 500: {end - start} seconds")
start = time.time()
quickSort(list1000[:], 0, len(list1000)-1)
end = time.time()
print(f"    N = 1000: {end - start} seconds")
start = time.time()
quickSort(list5000[:], 0, len(list5000)-1)
end = time.time()
print(f"    N = 5000: {end - start} seconds")
