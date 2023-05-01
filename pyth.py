# Write a Python function that takes two arguments (a and b) and returns their sum.
def sum_a_and_b(a,b):
    sum=a+b
    return sum
print(sum_a_and_b(20,24))
# Write a Python function that takes a string as input and returns the string reversed.
def reversed_string(word):
    word="".join(reversed(word))
    return word
print(reversed_string("akirachix"))

# Write a Python function that takes a list of integers as input and returns 
# the sum of all the integers in the list.
def sum_intergers(nums):
    sum=0
    for i in nums:
        sum+=i
    return sum
print(sum_intergers([1,2,5,3,6]))

# Write a Python function that takes a list of integers as input and 
# returns a new list with all the even numbers removed.
def removed_even_numbers(nums):
    for n in nums:
        if n % 2==0:
            nums.remove(n)
    return nums          
print(removed_even_numbers([1,2,3,4,5,6,7,8,9]))
        
# Write a Python function that takes a list of integers as input and 
# returns the highest value in the list.
def highest_value(numlist):
    for x in numlist:
        if x in numlist:
          x=max(numlist)
          return x
print(highest_value([2,6,4,32]))

# Write a Python function that takes a list of strings as input 
# and returns a new list with all the strings capitalized.
def capitalized_string(names):
    # for name in names:
    #     if name in names:
    #         name=name.capitalize()
    # return name
    return [name.capitalize() for name in names]
print(capitalized_string(["hello","i","am","learning","python"]))
