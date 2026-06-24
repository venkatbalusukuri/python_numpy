import numpy as np
#indexing
arr=np.array([1,2,3,4])
print(arr[0]) # for 1-d array
#for 2-d array
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1[0,2]) #here arr[row,index] its like matrix
#for 3d array
arr2=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr2)
print(arr2.ndim) #to check the dimension
print(arr2[0,0,1]) #arr[first_dimension,second_dimentsion,column]
'''
Example Explained
arr[0, 1, 2] prints the value 6.

And this is why:

The first number represents the first dimension, which contains two arrays:
[[1, 2, 3], [4, 5, 6]]
and:
[[7, 8, 9], [10, 11, 12]]
Since we selected 0, we are left with the first array:
[[1, 2, 3], [4, 5, 6]]

The second number represents the second dimension, which also contains two arrays:
[1, 2, 3]
and:
[4, 5, 6]
Since we selected 1, we are left with the second array:
[4, 5, 6]

The third number represents the third dimension, which contains three values:
4
5
6
Since we selected 2, we end up with the third value:
6

'''
#negative indexing
arr3=np.array([[1,2,3,4],[5,6,7,8]])
print(arr3[0,-1]) #w can get last element from the first row negative index starts from last 
