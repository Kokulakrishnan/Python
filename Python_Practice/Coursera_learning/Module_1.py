'''
Created on May 3, 2020

@author: KOKULAKRISHNAN
'''
"""
from unittest.test.testmock.testpatch import function
from builtins import False, True, None
"""
"""

Module 1 includes 

    2. Expressions
    3. Conditional Statements 
    
#writing Paragraphs of Code

name = input('Enter File:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(words, 0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
        
print(bigword, bigcount)

        
"""
"""
#Converting User Input

inp = input('Europe Floor')
usf = int(inp) + 1
print('US floor', usf) 

"""

"""
Conditional Statements
increase / maintain after if or for 
"""
"""
x = 5
if(x>2):
    print("Bigger than 2")
    print('Still Bigger')
print('Done with 2')

for i in range(5):
    print(i)
    if(i>2):
        print('Bigger than 2')
    print('Done with i', i)
print('All done')

"""

"""
3.2 More Conditional Statements
-------------------------------
 here we discussed about try and except
 
"""
"""
astr = 'hello bob'
try:
    istr = int(astr)
except:
    istr = -1
    
print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
    
print('second', istr)
"""

"""
4.1 Functions
-------------
"""
"""
def thing():
    print('hello')
    print('fun')

thing()
print('Zip')
thing()
"""

"""
x = 5
print('Hello')

def print_lyrics():
    print("T'm a lumberjack, and I'm okay.")
    print('I Sleep all night and I work all day")
print('Yo')
print_lyrics()
x = x + 2
print(x)
"""

"""
passing values for the parameters in the function

"""
"""
def greet(lang):
    if lang == 'es':
        print('Hola")
    elif lang = 'fr':
        print('Bonjour')
    else:
        print('Hello')
        
greet('en')
greet('es')
greet('fr')
"""
#-----------returning values in functions---------
"""
def greet():
    return "hello"
    
print(greet(), "Glenn")
print(greet(), "Sally")
"""

#5.1 Loops and Iteration

#_-------While Loop-----------

"""
n = 5 
while n>0:
    print(n)
    n = n-1
print('Blastoff')
print(n)
"""

#---------------Breaking out of loop-------

"""
while True:
    line = input('>')
    if line == 'done'
        break
    print(line)
    
print('Done!')
"""

#------------Finishing iteration with continue---

"""
while True:
    line = input('>')
    if line[0] == '#':
        continue
    if line == 'done'
        break
    print(line)
print('Done!')
"""

#-----------Finite Loops / Definite Loops-------

"""
Friends = ['joseph', 'Glenn', 'Sally']
for friend in Friends:
    print('Happy New Year', friend)
print('done!')
"""

#Finding the largest value using For loop
"""
largest_so_far = -1
print('before', largest_sor_far)
for the_num in [9,41,12,3,74,15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print('largest_so_far', the_num)

print('after', largest_so_far)
"""

#--------5.4 Loop Idioms---------------

#counting in a loop
"""
zork = 0 
print('Before', zork)
for thing in [9,41,12,3,74,15]:
    zork = zork + 1
    print(zork, thing)
print('After', zork)
"""

#summing in a loop
"""
tot = 0 
print('Before', zork)
for thing in [9,41,12,3,74,15]:
    tot = tot + thing
    print(zork, thing)
print('After', zork)
"""

#Finding the average in a loop
"""
count = 0 
sum = 0 
print('Before', count, sum)
for value in [9,41,12,3,74,15]:
    count = count+1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum/count)
"""

#Filtering in a Loop
"""
print('Before')
for value in [9,41,12,3,74,15]:
    if value > 20:
        print('Large number', value)
    else:
        print('small Number', value)
print('After')
"""

#search using a boolean variable
"""
found = False
print('Before', found)
for value in [9,41,12,3,74,15]:
        if value == 3:
            found = True
        print('Found', found)
print('After', found)
"""

#finding smallest value using for loop
"""
smallest = None
print('Before')
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = value
    elif smallest > value:
        smallest = value
    print(smallest, value)
print('After', smallest)
"""

