import numpy as np

class Upflairs:
    def __init__(self, arrLen, arr):
        self.arrLen = arrLen
        self.arr = arr 

    def get(self):
        try:
            for i in range(self.arrLen):
                self.arr.append(float(input(f'Enter element at index {i}: ')))
        except ValueError:
            print('Input should be integer or float value!')
            exit()
        return np.array(self.arr)
    
    def mean(self,array):
        sum = 0
        for i in array:
            sum +=i
        return sum/self.arrLen
    
    def median(self,array):
        mid = 0
        if self.arrLen % 2 != 0:            
            mid = array[self.arrLen//2]
        else:
            mid1 = arr[self.arrLen//2]
            mid2 = arr[(self.arrLen-1)//2]
            mid = (mid1 + mid2)/2
        return mid


try:
    arrLen = int(input('Enter the length of the array: '))
    arr = []
except ValueError:
    print("Please check your input!")
    exit()

obj = Upflairs(arrLen, arr)
array = obj.get()
mean = obj.mean(array)
median = obj.median(array)
print(f'\nMean of {array} is {mean}.')
print(f'Mean of {array} is {median}.')