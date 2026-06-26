#print('This is my second assignment!')

#This is an additional code I've written
#print('We are living in yellow submarine')

s = 'Hello World!'
print(s[0])
print(s[2:5])
print(s[3:])
print(s*2)
print(s+'Everyone!')
print(s.lower())
print(s.replace('l','s'))
print(len(s))
print(s.strip())
print(s.split(' '))

MyInteger= 10
print(type(MyInteger))

# Converting integer to String
integerToStr = str(MyInteger)
print("Integer into String: ", integerToStr)
print(type(integerToStr))

#initializing and declaring variable and value
floatNumberOne=11.10
floatNumberTwo = 2/5
print(floatNumberOne)
print(floatNumberTwo)

# checking data type
print(type(floatNumberOne))
print(type(floatNumberTwo))

# Converting float to String
MyStringOne = str(floatNumberOne)
MyStringTwo = str(floatNumberTwo)

print("Floating point into String: ", MyStringOne)
print("Floating point into String: ", MyStringTwo)

# checking data type
print(type(MyStringOne))
print(type(MyStringTwo))

mylist=[] # create a empty list
print(mylist)

# Create a list of strings.
string_list = ["Hello", "Python", "World"]
print(string_list)

# Create a list of numbers.
number_list = [3, 4, 5, 6, 8, 10]
print(number_list)

# Create a list of boolean values.
boolean_list = [True, False, False, True]
print(boolean_list)

# Create a mixed list or list with heterogeneous data
mixed_list = [3, 4, "Python", True]
print(mixed_list)

# Create a string.
my_string = "Hello World"

# Create a list of characters from my_string.
character_list = list(my_string)

# Create a list of substrings from my_string.
substring_list = my_string.split()

# Print the results.
print(my_string)        # Output: "Hello World"
print(character_list)   # Output: ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
print(substring_list)   # Output: ['Hello', 'World']

# Create a list.
my_list = [1, 2, 3, 4, 5]
print("before:",my_list)

# Modify an element in the list.
# Note that the first element in
# a list is at index 0.
my_list[2] = 7
# Print the result.
print("after:", my_list)  # output: [1, 2, 7, 4, 5]

my_list = [1, "Hello Python", 7.98]
# Output: 'Hello Python'
print("before: ", my_list[1])

# Output: 'Hello JavaScript'
my_list[1] = "Hello JavaScript"
print("after: ", my_list[1])

my_list1 = [1,2,3,4]
print(my_list)

my_list1.insert(2,3)
print(my_list1)
my_list1.insert(1,67)
print(my_list1)

my_groceries = ['avocado', 'mango', 'lip balm', 'sunglasses']
my_wife_groceries = ['New dining table', 'new sports', 'facemasks']
combined_groceries = my_groceries + my_wife_groceries

print(combined_groceries)

#Create a list.
my_list = [1, 2, 3, 4, 5]
#Traverse the list with a for loop. 
for element in my_list:   
    print(element)
#Traverse the list by accessing the
# indexes with the range() and len() functions.
for i in range(len(my_list)):   
    print(f'Index {i} contains: {my_list[i]}')

# Create a two-dimensional list with three sublists.
# Each sublist contains three elements.

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Print the middle element of the 2D list.
# Remember that list indexes start at 0.
print(my_list[1][1])        # output: 5

# Create a two-dimensional list with three sublists.
# Each sublist contains three elements.
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Iterate through each sublist.
for sublist in my_list:
# Iterate through each sublist element.
    for element in sublist:     
        print(element)
# output (each on a new line): 1 2 3 4 5 6 7 8 9

nums = [1, 2, 3, [4, 5, 6, [7, 8, [9]]], 10]

print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4])
print(nums[3][3][2])




