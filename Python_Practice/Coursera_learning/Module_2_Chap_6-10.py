'''
Created on May 3, 2020

@author: KOKULAKRISHNAN
'''
#---------------------7.1 Files----------------
'''
from importlib.resources import contents
from audioop import reverse
from builtins import True
'''
#How to open a file
"""
fhand = open('mobox.txt')
print(fhand)
"""

#---------------------7.2 Processing Files------

#File handle as a sequence
"""
xfile = open('D:\office Drive\Capgemini\learnings\Python Traning\handson\Dataset\count_sum_numbers_sample_data.txt')
for cheese in xfile:
    print(cheese)
"""

#counting Lines in a file 
"""
fhand = open('D:\office Drive\Capgemini\learnings\Python Traning\handson\Dataset\count_sum_numbers_sample_data.txt')
count = 0
for lines in fhand:
    count = count + 1
print(count)
"""

#reading the whole file
"""
fhand = open('D:\office Drive\Capgemini\learnings\Python Traning\handson\Dataset\count_sum_numbers_sample_data.txt')
inp = fhand.read()
print(len(inp))

print(inp[:20])
"""

#searching through a file
"""
fhand = open('D:\office Drive\Capgemini\learnings\Python Traning\handson\Dataset\count_sum_numbers_sample_data.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)
"""  

#removing space in right and left side of string
"""
fhand = open('D:\office Drive\Capgemini\learnings\Python Traning\handson\Dataset\count_sum_numbers_sample_data.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
            print(line)
"""

#skiping with continue
"""
fhand = open('D:\office Drive\Capgemini\learnings\Python Traning\handson\Dataset\count_sum_numbers_sample_data.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)
"""

#-----------------8.1 Lists---------------------------
"""
#How to define a list 
friends = ['Joseph', 'Glenn', 'sally']
print(friends)
"""

#How long is a list
"""
greet = 'Hello Bob'
print(len(greet))

x = [1,2,'jo2', 99]
print(len(x))
"""

#using range function in list
"""
print(range(4))

friends = ['Joseph', 'Glenn', 'sally']
print(len(friends))

print(range(len(friends)))
"""

#tale of two loops 
"""
friends = ['Joseph', 'Glenn', 'sally']

for friend in friends:
    print('Happy new year', friend)
    
for i in range(len(friends)):
    friend = friends[i]
    print('Happy new year', friend)
"""

#----------------8.2 Manipulating Lists--------

#How to concatenate list using +
"""
a = [1,2,3]
b = [4,5,6]
c = a + b

print(c)
"""

#List slicing is also be possible like string
"""
t = [9,41,12,3,74,15]
print(t[1:3])
#in above print statement, the second number is "uptp but not included"
"""

#Building list from scratch 
"""
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)

stuff.append('cookie')
print(stuff)

stuff.append('Cookies')
print(stuff)
"""

#How to sort a list 
"""
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)
print(friends[1])
"""

#other built in functions
"""
nums = [3,41,12,9,74,15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/ len(sums))
"""

#getting numbers in the list and coming out when done
"""
numlist = list()
while True:
    inp = input('Enter a number')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
    
average = sum(numlist) / len(numlist)
print('average', average)
"""

#------------8.3 List & Strings-----------

#best friends: strings and lists
"""
abc = 'with three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

print(stuff)
for w in stuff:
    print(w)
""" 

#another example 
"""
line = 'A lot           of space'
etc = line.split()
print(etc)

line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))

thing = line.split(':')
print(thing)
print(lent(thing))
"""

#finding which day the email was sent from a file

fhand = open('D:\office Drive\Capgemini\learnings\Python Traning\handson\Dataset\mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])
 

#double split pattern
"""
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
"""

#-------------------9.1 Dictonary-------------------------

#Dictionaries
"""
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75

print(purse)
"""

#Dictionaries are mutable
"""
purse['candy'] = purse['candy'] + 2
"""

#many counters with a dictionary 
"""
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)

ccc['cwen'] = ccc['cwen'] + 1
print(ccc)
"""

#Dictionary Tracebacks
"""
it is an error to reference a key which is not in dictionary
we can use the 'in' operator to see if a key is in the dictionary
"""
"""
ccc = dict()
print(ccc['csev])
"""

#when we see a new name
""" 
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
"""

#the get method for dictionaries 
"""
the pattern of checking to see if a key is already in 
a dictionary and assuming a default value if the key is
not there is a common that there is a method called 
'get()' that does this for us 
"""

"""
counts = dict()
#names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
names = ['csev']
for name in names:
    if name not in counts:
        x = counts[name]
    else:
        x = 0
print(counts)

x = counts.get(name, 0)
print(x)
"""

#simplified counting with get()
"""
we can use 'get() and provide a default value of zero
when the key is not yet in the dictionary - and then
just add one
"""
"""
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwan']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
"""

#9.3 Dictionaries and Files (counting pattern)
"""
The general pattern to count the words in a line 
of text is to split the line into words, then loop 
through the words and use a dictionary to track the 
count of each word independently.
"""
"""
counts = dict()
print('Enter a line of text:')
line = input('')
words = line.split()
print('words:', words)

print('Counting....')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('counts', counts)
"""

#definite loops and dictionaries

'''
even though dictionaries are not stored in order, 
we can write a for loop that goes through all the 
entries in a dictionary - actually it goes through
all of the keys in the dictionary and looks up the 
values
'''
'''
counts = {'chuck': 1, 'freed': 42, 'Jan': 100}
for key in counts:
    print(key, count[key])
    
'''

#retrieving lists of keys and values from dictionaries
'''
jjj =  {'chuck': 1, 'freed': 42, 'Jan': 100}
print(jjj.values())
print(jjj.keys())
print(jjj.items()) #it is tuple
'''
    
#two iteration variables
'''
jjj = {'chuck': 1, 'freed': 42, 'Jan': 100}
for key, value in jjj.items():
    print(key,value)
'''

#now we will understand the program that we saw firtst
'''
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
'''

#-------10. Tuples----------------------------

'''
unlike a list, once you create a tuple, you cannot alter its
contents
'''
'''
x = (3,2,1)
x.sort()
x.append(5)
x.reverse()
'''
'''
in tuple you cannot apply inbuilt functions of list
''' 

#tuples and dictionaries
'''
The 'items() method in dictionaries returns a list
of (key, value) tuples
'''
'''
d = dict()
d['csev'] = 2
d['cwen'] = 4

for (k,v) in d.items():
    print(k,v)
    
tup = d.items()
print(tup)
'''

#sorting lists of tuples

'''
we can take advantage of the ability to sort a list
of tuples to get a sorted version of dictionary 

first we sort the dictionary by the key using the items()
mehtod and sorted() function
'''
'''
d ={'a':10, 'b':1, 'c':22}
d.itmes()
t = sorted(d.items())
print(t)
for k,v in sorted(d.items()):
    print(k.v)
'''

#sorting by values instead of key 

'''
if we could construct a list of tuples of the form (value, key)
we could sort by value 

we do this with a for loop that creates a list of tuples
'''
'''  
c = {'a':10, 'b':1,'c':22}
print(c)
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)
'''

#Another example
'''
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[words] = counts.get(word, 0) + 1
    
lst = list()
for key, val in counts.items():
    newtup = (val,key)
    lst.append(newtup)
    
lst = sorted(lst,reverse= True)
for val, key in lst[:10]:
    peint(key, val)
''' 

#to have even shorter version
'''
c = {'a':10, 'b':1,'c':22}
print(sorted([(v,k) for k,v in c.items()], reverse = True))   
'''