# If statements
# An If statement is used to compare things

#variable = input('This is an input thta will take a response')
#print(variable)

# Going to ride the conay island roller coaster
# 4' aka 48'
#height = int(input('How tall are you? '))
# height >= 48
#if height >= 48:
    #print('You may ride')
#else:
    #print('Sorry kid, get lost, come back next year')

# create a password checker
# username = HotDogWater123
# password = bluepon

#password = 'bluepon'

#userLoginInput = input('Enter password: ')

#if userLoginInput == password:
    #print('Open Sesame')
#else:
    #print('Access denied')

# check if number is even or odd
#number = int(input('Enter a number: '))

#if number % 2 == 0:
    #print('Even')
#else:
    #print('Odd')

# Write a for loop for the value 1- 152
# numebrs =[1,2,3,4,...]
#for number in range(1,153):
    #print(number)

# countdown from 10-0
for number in range(10, 0, -1):
    print(number)
print('Blast off!')

# Who likes root beer?
numberOfRootBeers = 31

for i in range(numberOfRootBeers, 1, -1):
    print(f'{i} bottles of root on the wall...')
    print(f'{i} bottles of root beer')
    print('take on down, pass it around...')
    print(f'{i-1} bottles of root on the wall...')

# What is the sum of 1-427

total = int(input('Pick a number to add up to: '))

for number in range(1,428):
    total += number
print(f'Your total in: {total}')

#update if statement  to while loop so that users can have multiple attempts

password = 'Hello'
userLoginInput = input('Enter password: ') 

while userLoginInput != password:
    print('Wrong password - please try again ')
    userLoginInput = input('Enter password ')
print('Open Sesamo')

#Find the largest number
numberList = [1, 4, 6, -4, 1000, 9, 56, 789]

#First number in this case is 7 

largestNumber = numberList[0]

for number in numberList:
    # first iteration says 'Is 7 larger than 7? if not move on to second iteration, if so... then the new largest number
    # becomes the value we´re checking in the list
    if number > largestNumber:
        largestNumber = number
print(largestNumber)

#Who wants to play... GUESS THAT NUMBER!
secretNumber = 2

guess = 0

while guess != secretNumber:
    guess = int(input('Guess the secret number: '))
print('You got it!')




