# 1. Write a Python program to get a single string from two given strings, separated by a space,
#  and swap the first two characters of each string
def get_single_string(str1,str2):
   x_str1=str2[:2] + str1[2:]
   x_str2=str1[:2] + str2[2:] 
   return x_str1 + " " + x_str2  
print(get_single_string("annita","hopper"))


# 2.Write a Python function that takes a list of words and returns the longest word 
# and the length of the longest one
def longest_word(words):
    count=0
    for n in words:
        if len(n) >=count:
            count=len(n)
            return count
print(longest_word(["AkiraChix","Nairobi","Kenya"]))


# 3. Write a Python program that accepts a comma-separated sequence of words as input 
# and prints the distinct words in sorted form (alphanumerically).


# 4.. Write a Python function that takes two lists and returns True if they have at 
# least one common member.
def common_member(list1,list2):
    result=False
    for x in list1:
     for y in list2:
        if x==y:
            result=True
            return result
print(common_member([1,2,3,4,5],[5,6,7,8,9]))


# 5. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]

color_name=["Black", "Red", "Maroon", "Yellow"]
color_code=["#000000", "#FF0000", "#800000", "#FFFF00"]
convert_to_dictionary=dict(zip(color_name,color_code))
print(convert_to_dictionary)

# 6. Write a Python program to check whether all dictionaries in a list are empty or not
list_d=[{},{},{}]
print(all(not x for x in list_d))

list_d1=[{1:"John"},{2:"James"},{3:"Joh"}]
print(all(not x for x in list_d1))


# 7. Given a list of numbers, use list comprehension to remove all odd numbers from the list:

numbers = [3,5,45,97,32,22,10,19,39,43]
remove_odd_numbers=[n for n in numbers if n % 2==0]
print(remove_odd_numbers)

# 8. Find the common numbers in two lists (without using a tuple or set) 
list_a = 1, 2, 3, 4, 
list_b = 2, 3, 4, 5
common_numbers=[z for z in list_a if z in list_b]
print(common_numbers)

# 9. Use a nested list comprehension to find all of the numbers from 1-1000 
# that are divisible by any single digit besides 1 (2-9)

all_numbers=list(range(1,1000))
single_digit_divisors=list(range(2,9))
y = [number for number in range(1,1000) if True in [True for x in range(2,9) if number % x == 0]]
print(y)

# 10. Write a Python function to remove all vowels in a string

def remove_vowels(word):
    vowels=["a","e","i","o","u"]
    x=[letter for letter in word if letter.lower() not in vowels]
    x=''.join(x)
    return x
print(remove_vowels("Angeth"))






