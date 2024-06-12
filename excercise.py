

def sum(list):
    if  len(list)==1:
        return list[0]
    else:
        return list[0]+sum(list[1:])
    

def recursiveListSum(dataList):
    total = 0
    for element in dataList:
        if type(element) == type([]):
            total += recursiveListSum(element)
        else:
            total = total + element
    return total
# 4. Write a Python program to get the factorial of a non-negative integer using recursion.
def factrial(num):
    if num<=1:
        return 1
    else:
        return num*factrial(num-1)
# 5. Write a Python program to solve the Fibonacci sequence using recursion.
def fibonaci_squence(num):
    if num ==0 or num==1 or num==2 :
        return 1
    else:
        return fibonaci_squence(num-1)+fibonaci_squence(num-2)
    
def sumDigit(num):
     if num==0:
         return 0
     else:
         return num%10+sumDigit(num//10)
     
# 7. Write a  Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0) using recursion .  
def sum_series(num):
    if num<0:
        return 0
    else:
        return num+sum_series(num-2)

# 8. Write a  Python program to calculate the sum of harmonic series upto n terms.
def harmony_series(num):
    if num<2:
        return 1
    else:
        return 1/num+harmony_series(num-1)

# Write a Python program to calculate the geometric sum up to 'n' terms.
def geometric_sum(num, a=1, r=0.5):
    if num == 0:
        return 0
    else:
        return a * r**(num-1) + geometric_sum(num-1, a, r)
#  Write a Python program to calculate the value of 'a' to the power of 'b' using recursion
def power(a,b):
    if b==0:
        return 1
    elif a==0:
        return 0
    elif b==1:
        return a
    else:
        return a*power(a,b-1)
    
#  Write a  Python program to find the greatest common divisor (GCD) of two integers using recursion.
def GCF(num1, num2):
    if num2==0:
        return num1
    else:
       return  GCF(num2,num1%num2)

print("sum",sum([1,2,3,4,5]))
print("Sum recursive",recursiveListSum([1,2,[3,4,5],6,7]))
# print(factrial(5))
# print(sumDigit(120))
# print(sum_series(10))
# print(harmony_series(7))
print(geometric_sum(6))
print(power(3,4))
print(GCF(48,18))