import numpy as np
#o-d array
arr=np.array(20)
print(arr)
print(type(arr))
#1-d array
arr1=np.array([1,2,3,4])
print(arr1)
#2-d array
arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)
#3-d array
arr3=np.array([[[1,2,3],[4,5,6]],[[8,9,10],[11,12,13]]])
print(arr3)
#n-d n no.of dimensions
arr4=np.array([1,2,3,4],ndmin=4) #ndmin =n where n refers to no.of dimensions we required
print(arr4)
#to check no.of dimession does array have
#we use ndim return integer valueas no.of dimensions
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)
