class algorithms:
    def __init__(self):
        pass
    def bubbleSort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-j-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1] , arr[j]
                    