
from array import *
#  # type: ignore

# array_num = array("i",[1,2,3,4,5,6,7,7,8,9])

# for i in array_num:
#     print(i)

# array_string =["Gashaw","Gedef","Shibabaw","Tadege","Kassa"]
# print(array_string)



# #### Write a Python program to append a new item to the end of the array.
# array_2 = array("i",[1,2,3,4,5,6,7,7,8,9])
# array_2.append(90)
# print(array_2)


# ###Write a  Python program to reverse the order of the items in the array.

# array_3 =array("i",[3,45,6,87,9,45])
# # reversed_array = array_3[::-1]
# reversed_array2 = array_3.reverse()
# # print(reversed_array)
# print(str(reversed_array2))

# # Write a  Python program to get the length in bytes of one array item in the internal representation.

# array_4 =array("i",[3,45,6,87,9,45])
# print(array_4.itemsize)

# #Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array's contents. Also, find the size of the memory buffer in bytes.
array_5 = array('i', array('i', [1, 3, 5, 7, 9]))
array_5.insert(5,98)
print(array_5)


# def accessElementOfArray(array,index):
#     if index > len(array):
#         print("There is no such index")
#     else:
#         print(array[index])


# accessElementOfArray(array_5,2)



# ###Searching Algorithims
# def searchAnElement(array, element):
#     found = False
#     for i, num in enumerate(array):
#         if num == element:
#             print("Found at index:", i)
#             found = True
#             break
#     if not found:
#         print("The element was not found")

# searchAnElement(array_5,5)


# def removeArrayElement(array, value):
#     if not array:  # Checking if the array is empty
#         print("Array is Empty")
#     elif value not in array:  # Checking if the value exists in the array
#         print("Value", value, "is not present in the array")
#     else:
#         array.remove(value)
#         print("Value", value, "removed from the array")

# removeArrayElement(array_5,5)
# print("After removed",array_5)
