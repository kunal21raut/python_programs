from numpy import *
arr1=array([1,2,3,5,6,6])

arr2 = arr1

print("arr1:",arr1,"\narr2:",arr2)
print("address of arr1:",id(arr1),"\naddress of arr2:",id(arr2))

#shallow COpy
print("shallow COpy")
arr1=array([1,2,4,9,8])



arr2 = arr1.view() #view method is used for shallow copy
arr1[2]=77
print("arr1:",arr1,"\narr2:",arr2)
print("address of arr1:",id(arr1),"\naddress of arr2:",id(arr2))

#Deep COpy
print("Deep COpy")
arr1=array([1,2,4,35,8])
print('Deep Copy')


arr2 = arr1.copy() #copy method is used for shallow copy
arr1[0]=24

print("arr1:",arr1,"\narr2:",arr2)
print("address of arr1:",id(arr1),"\naddress of arr2:",id(arr2))
