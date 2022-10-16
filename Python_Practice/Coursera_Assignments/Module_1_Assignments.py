'''
Created on May 3, 2020

@author: KOKULAKRISHNAN
'''
"""
# the code below almost works
print("hello world")
"""

"""
#assignment 2.2

# The code below almost work

user = input('Enter your name')
print('Hello',user)
"""

"""
assignment 2.3

2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
You should use input to read a string and float() to convert the string to a number. 
Do not worry about error checking or bad user data.
"""
"""
# This first line is provided for you

hrs = input("Enter Hours:")
rate = input("Enter rate:")
print("Pay:", float(hrs)*float(rate))

"""
"""
3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 
hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use input to read a string and float() to convert the string to a number.
Do not worry about error checking the user input - assume the user types numbers properly
"""

"""
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
if(h>40):
    print((40*r)+((h-40)*r*1.5))
else:
    print(h*r)
"""

"""
3.3 Write a program to prompt for a score between 0.0 and 1.0. 
If the score is out of range, print an error. If the score is between 0.0 and 1.0, 
print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. 
For the test, enter a score of 0.85.
"""
"""
score = input("Enter Score: ")
s = float(score)
try:
    if((s>=0.9) and (s<=1.0)):
        print("A")
    elif(s>=0.8):
        print("B")
    elif(s>=0.7):
        print("C")
    elif(s<0.6):
        print("D")
    else:
        print("F")
except:
    print("Invalid Number")
"""

"""
4.6 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours
worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() 
and use the function to do the computation. The function should return a value. Use 45 hours and 
a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use input to read a string and float() to convert the string to a number. Do not worry 
about error checking the user input unless you want to - you can assume the user types numbers properly. 
Do not name your variable sum or use the sum() function.
"""
"""
def computepay(h,r):
    if(h>40):
        pay = ((40*r) + (h-40)*r*1.5)
    else:
        pay = h * r
    return (pay)

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
p = computepay(h,r)
print("Pay",p)
"""

"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything 
other than a valid number catch it with a try/except and put out an appropriate message and 
ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
"""

"""
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        if num == "done" : break
        elif smallest is None:
            smallest = int(num)
        elif(smallest > int(num)):
            smallest = int(num)
        elif largest is None:
            largest = int(num)
        elif (largest < int(num)):
            largest = int(num)
    except:
        print("Invalid input")
        
print("Maximum is", largest)
print("Minimum is", smallest)
"""

num_list = list()
while True:
    num = input("Enter a number:")
    try:
        if num == "done": continue
        num_list.append(int(num))
    except:
        print("Invalid Number")
        
sort_list = sorted(num_list)
print("Maximum is", sort_list[len(sort_list)-1])
print("Minimum is", sort_list[0])

