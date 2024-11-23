import random
def bubbleSort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1] , arr[j]
def shuffleArray(arr):
    n = len(arr)
    for i in range(n):
        j = random.randint(0,n-1)
        arr[i], arr[j] = arr[j], arr[i]                    
                    