# from array import *

# val = array('i',[1,2,3,4,5,6,7,8,9])

# for i in range(0,len(val)):
#     print(val[i], end=" ")

# print('\n')

# for x in val:
#     print(x, end=" , ")

# print('\n')

# print(val.typecode)

# val.reverse()

# for i in range(0,len(val)):
#     print(val[i] , end=" ")

# val.insert(1,50)
# val.append(100)

# for i in range(0,len(val)):
#     print(val[i], end=" ")

# print('\n')
# copyArray = array(val.typecode, (a*3 for a in val))

# copyArray.pop(2)

# for i in range(0,len(copyArray)):
#     print(copyArray[i], end=" ")


# abc = val[2:-3]
# abc = val[::-1]

# for i in range(0,len(abc)):
#     print(abc[i], end=" ")

#Dynamic Array

# arr = array('i',[])

# n = int(input("Enter number of elements: "))

# for i in range(0,n):
#     x = int(input("Enter next element: "))
#     arr.append(x)

# for i in range(0,len(arr)):
#     print(arr[i], end=" ")

# arr = array( 'i' , [12,23,45, 234, 134, 235] )

# i = arr.index(405)

# print(i)

import numpy as np

# arr = np.array( [1,2,3,4,5,6,7,8,9] )

# print(arr)

# val = np.linspace(10, 20, 5 )

# for i in range(0,len(val)):
#     print(val[i], end=" ")

# val = np.arange(10, 50, 2)

# val = np.full(5, 7)

# for i in range(0,len(val)):
#     print(val[i], end=" ")

zero = np.array(5)
print(zero)

ones = np.array([3,4])
print(ones)

two = np.array([[1,2,3],[4,5,6], [7,8,9]])
print(two)

three = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
print(three)