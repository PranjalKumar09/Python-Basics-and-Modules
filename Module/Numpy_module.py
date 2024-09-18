""" 
numpy allows serval *mathematical operations * faster operations
numpy writtern in c so fast 
(numpy stands for numperical pythons)



numpy takes less memory than usual list 
even this takes less time than usual list

numpy.arange(num) It reates numpy array  like it will create this as [ 0,1,2 ... 19]

numpy.linspace([start , end , total_numbers]) => total_numbers are total number  that will created where starting  ending specified

usually remember that it is not line its lin so linspace


numpy.empty(size) -> create random numpy array of size size
size is tuple of size , it can 2d or 3d array too

numpy.empty_like(numpy_carry) -> create same numpy array

numpy.identity(num) => returns numoy array  (2d matrix) identity matrix

numpy.eye is same as identy but provide aditional option

numpy.eye(R, C = None, k = 0, dtype = type <‘float’>) : Return a matrix having 1’s on the diagonal and 0’s elsewhere w.r.t. k.

R : Number of rows
C : [optional] Number of columns; By default M = N
k : [int, optional, 0 by default]
          Diagonal we require; k>0 means diagonal above main diagonal or vice versa.
dtype : [optional, float(by Default)] Data type of returned array.



To get data type of any numpy array => np_array.dtype

numpy.shape(numpy.identity(num)) it is equal to (num , num)

array.reshape(shape) => it reshae the numpy of same data to respective shape
it can convert 2d , 3d etc)
but it will give error if shape not possible 


array.ravel() -> convert array to 1d array

there is axis also exist in numpy in 1d -> 1axis axis0
in 2d -> 2 axis axis0 axis1
in 3d -> 3 axis axis0 axis2

array.sum(axis = 0)
# explain => it sums all column in fist row

array.sum(axis = 1) 
# similarly it does for the first column

array.T => returns transpose of the original matrix
array.T and array.transpose()     are same  

array.flat => returns a matrix

array.ndim => returns the number of dimensions of the matrix

array.size => returns the total no of element in array even in 1d , 2d or 3d dimension

array.nbytes => retruns total byte consumed

array.argmax => returns the index having maximum element
array.argin => returns the index having the minimum element


array.argsort()

basically it returns the index postion having smallest element like this
it return array in same shape as of array (even in 2d)

now you want to in 2d max and min indexes
then use array.argmax() & array.argmin()

arrayh.argmax(axis = 0) # it returns the 1d array of same size 
arrayh.argmax(axis = 1) # it returns the 1d array of same size




Matrix addition
two matrics can be added only if they have same matrix similarly for subtraction


To perform matrix multiplication (matrix with matrix),  first matrix must have  same number of columns as  second matrix has rows  so size of result matrix will row of matix1 * column of matix2
 _      _       _       _     _                     _
| q    b |  *  | e    f |   =|  ae + bg      af + bh   |   
|_c    d_|     |_g    h_|    |_ ce + dg      cf + dh  _|   



+ ,- ,  / ., *    also work in these numpy array


numpy.add(a,b)
numpy.subtract(a,b)
numpy.multiply(a,b)
numpy.divide(a,b)

it returns in same date type as of a & b 

numpy.where(condtion , what when true, what when false)

array.tolist() => conver numpy array to list

to convert different data types (like list, tuple) to numpy array  => numpy.asarray(list or tuple) 




To fill from [0 , 1) => numpy.random.rand( shape) 


To make randomly fill numoy => numpy.random.randint(start , end , shape) 
shape in tuple
[start , end)



 numpy.flip(array, axis)


Parameters : 

array : [array_like]Array to be input 
axis  : [integer]axis along which array 
        is reversed.




numpy.ones(shape, dtype=None)
Return a new array of given shape and type, filled with 1

Parameters
    shapeint or sequence of ints
        Shape of the new array, e.g., (2, 3) or 2.
    dtypedata-type, optional
        The desired data-type for the array, e.g., numpy.int8. Default is numpy.float64

similarly there is also numpy.zeros 





numpy.insert(array, object, values, axis = None)
array   : [array_like]Input array. 
object  : [int, array of ints]Sub-array with the index or indices before 
     which values is inserted
values  : [array_like]values to be added in the arr. Values should be 
     shaped so that arr[...,obj,...] = values. If the type of values is different from 
     that of arr, values is converted to the type of arr
axis    : Axis along which we want to insert the values. By default, it 
     object is applied to flattened array    
     
     
     

"""

import imp
import numpy as np 


myarr = np.array([3 , 6 , -84 , 7] , np.int64)

""" 
Data Type in array
b   Boolean
f   Float
O   Object
U   Unicode String
i   Integer
u   Unsigned Integer
c   Complex Float
M   DateTime
S   String
V   A fixed chunk of memory for other types (void)

The list of various types of data types provided by NumPy are given below:

Data Type
-----
bool_      Boolean
int_       Default integer type (int64 or int32)
intc       Identical to the integer in C (int32 or int64)
intp       Integer value used for indexing
int8       8-bit integer value (-128 to 127)
int16      16-bit integer value (-32768 to 32767)
int32      32-bit integer value (-2147483648 to 2147483647)
int64      64-bit integer value (-9223372036854775808 to 9223372036854775807)
uint8      Unsigned 8-bit integer value (0 to 255)
uint16     Unsigned 16-bit integer value (0 to 65535)
uint32     Unsigned 32-bit integer value (0 to 4294967295)
uint64     Unsigned 64-bit integer value (0 to 18446744073709551615)
float_     Float values
float16    Half precision float values
float32    Single-precision float values
float64    Double-precision float values
complex_   Complex values
complex64  Represent two 32-bit float complex values (real and imaginary)
complex128 Represent two 64-bit float complex values (real and imaginary)

"""
""" 
print(myarr[0]) # 3

print(myarr.shape) # (4,)

myarr2 = np.array([[3 , 6 , -84 , 7] ], np.int64)

print(myarr2[0 , 1 ]) # 3

print(myarr2.shape) # (1, 4)

print(myarr2)#[  3   6 -84   7]]

rng = np.arange(20) 

print(rng) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

lspace = np.linspace(1,5,4)

print ( lspace) # [1.         2.33333333 3.66666667 5.        ]

emp = np.empty((4,6))

print(emp)

abc = np.empty_like(lspace)

print(abc)  # [1.         2.33333333 3.66666667 5.        ] """

newarr = np.identity(3) 
print(newarr)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]


# test = np.arange(99)

# test1 = test.reshape((3,33))

# print( test1)


array3d = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(array3d) 
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]


print(array3d.sum(axis = 0)) # [12 15 18] 
# explain => it sums all column in fist row

print(array3d.sum(axis = 1)) # [ 6 15 24]
# similarly it does for the first column


print(array3d.flat) # numpy.flatiter object at 0x55e29969d3e0>

for i in array3d.flat:
    print(i)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

print(array3d.ndim) # 2

print()

print(array3d.size) # 9
print(array3d.nbytes) # 72 
print(array3d.argmax()) # 8
print(array3d.argmin()) # 0

array3d = np.array([[2,22,8],[5,51,16],[42,24,1]])

print(array3d.argsort()) 
# [[0 2 1]
#  [0 2 1]
#  [2 1 0]]
# basically it returns the index postion having smallest element like this

print ()
print ()


print(array3d.argsort(axis = 0))
# [0 0 2]
#  [1 2 0]
#  [2 1 1]]

print(array3d.argsort(axis = 1))
# [[0 2 1]
#  [0 2 1]
#  [2 1 0]]



print(array3d.argmin()) # 8
print(array3d.argmax()) # 0

print(array3d.argmin(axis= 0)) # [0 0 2]
print(array3d.argmax(axis= 1)) # [1 1 0]



print(array3d.ravel()) # [ 2 22  8  5 51 16 42 24  1]

array1 =  np.array([[2,22,8],[5,51,16],[42,24,1]])
array2 =  np.array([[12,24,18],[15,5,14],[2,29,31]])

print(array1 + array2)
# [[14 46 26]
#  [20 56 30]
#  [44 53 32]]



print(array1 * array2)
# [[ 24 528 144]
#  [ 75 255 224]
#  [ 84 696  31]]



print(np.sqrt(array2))
# [[3.46410162 4.89897949 4.24264069]
#  [3.87298335 2.23606798 3.74165739]
#  [1.41421356 5.38516481 5.56776436]]


print(np.max(array2))  # 31
print(np.min(array2)) # 2
print( np.sum(array2)) # 150


print(np.where(array2 < 20 , array2 , array2+5 ) ) 
# [[12 29 18]
#  [15  5 14]
#  [ 2 34 36]]


print(np.count_nonzero(array2)) # 9



non__numpy_array_list = [1,2,3,4,5,6,7,8,9,10,11]

numpy_array_list = np.array(non__numpy_array_list)

import sys 

print (sys.getsizeof(1) * len(non__numpy_array_list)) # 308



print (numpy_array_list.size * numpy_array_list.itemsize ) # 56

# so by this we can say numpy takes less memory than usual list 

print(array2.tolist()) #[[12, 24, 18], [15, 5, 14], [2, 29, 31]]



"""
from time import process_time

python_list = [i for i in range(10000)]

start_time = process_time()

python_list = [i+5 for i in python_list ]

end_time = process_time()

print(end_time - start_time)


np_array = np.array([i for i in range(10000)])

start_time2 = process_time()

np_array += 5 

end_time2 = process_time()

print(end_time2 - start_time2)


"""


print(np.eye(4))
print(np.eye(5))



arr = np.array([1, 2, 3 , -1])

# Calculate the exponential of each element
result = np.exp(arr)

print (result) # [ 2.71828183  7.3890561  20.0855369  20.36787944]
