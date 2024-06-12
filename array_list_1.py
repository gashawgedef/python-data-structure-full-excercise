
# numDays = int(input("How many day's Temprature?"))
# total = 0
# temp = []
# for i in range(numDays):
#     nextDay = int(input("Day"+str(i+1)+"'s high temp"))
#     temp.append(nextDay)

#     total += temp[i]

# avg = round(total/numDays,2)
# print("\nAverage:",str(avg))
# above = 0

# for i in range(len(temp)):
#     if avg >temp[i]:
#         above +=1 
         
# print(str(above)+" day(s) above average")
from array import *

def missingNumber(list, n):
    expectedSum = n*(n+1)/2
    actualSum = sum(list)

    misingNumber =expectedSum - actualSum
    return misingNumber


print(missingNumber([1,2,3,4,5],6))
    
def findPairSum(list,target):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i] == list[j]:
                continue
            elif list[i] + list[j]==target:
                print([i,j])

findPairSum([0,1,2,3,4,5,6],6)


myArray = array("i",[1,2,3,4,5,6 ])


def findNumber(list,number):
    for i in range(len(list)):
       if list[i] == number:
           print(i)


findNumber(myArray,78)

def maxProduct(list):
    maxP = 1
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if maxP <list[i] * list[j]:
                maxP = list[i]*list[j]
    return maxP
    

print("maximum Product is:",maxProduct(myArray))


def isUnique(list):
    a = []
    for i  in list:
        if i in a:
            return False
        else:
            a.append(i)
    return True

print(isUnique([1,2,3,4,5,6,6]))



###Write a function to remove duplicates


def removeDuplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list


print(removeDuplicates([1,2,2,2,3,3,4,5,6,6]))