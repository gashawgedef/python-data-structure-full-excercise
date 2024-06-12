

from array import *

array_num = array("i",[1,2,3,4,5,6,7,8,9])
array_num_2 = array("i",[12,13,14,15])
gashity_num = [20,30,56]
for i in array_num:
    print(i)
print(array_num[3])


array_num.append(10)
print("After Append",array_num)

array_num.insert(10,11)
print("After Insert",array_num  )

array_num.extend(array_num_2)
print("After Extend",array_num )


array_num.fromlist(gashity_num)
print("After From List",array_num)

value_list = array_num.tolist()
print("value list",value_list)

beffer_info = array_num.buffer_info()
print("Buffer Info:",beffer_info)

to_string = str(array_num)
print("To String",to_string)