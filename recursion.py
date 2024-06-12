#  Write a  Python program to calculate the sum of a list of numbers using recursion.


def calculate_sum_recursion(nums):

    if len(nums) == 0:
        return 0
    else:
        return nums[0]+calculate_sum_recursion(nums[1:])


print("Sums:",calculate_sum_recursion([10,2,3,4,5,6,7,8]))
# 4. Write a Python program to get the factorial of a non-negative integer using recursion.
def calculate_factorial(num):
    if num <= 1:
        return 1
    else:
        return num*calculate_factorial(num-1)
    

print("factorial:",calculate_factorial(6))


#  Write a Python program to solve the Fibonacci sequence using recursion.
def fibonacci(n):
    # Check if n is 1 or 2 (base cases for Fibonacci)
    if n == 1 or n == 2:
        # If n is 1 or 2, return 1 (Fibonacci sequence starts with 1, 1)
        return 1
    else:
        # If n is greater than 2, recursively call the fibonacci function
        # to calculate the sum of the (n-1)th and (n-2)th Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Print the result of calling the fibonacci function with the input value 7
print(fibonacci(7))
