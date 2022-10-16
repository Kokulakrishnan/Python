'''
Created on May 3, 2020

@author: KOKULAKRISHNAN
'''
"""
7.1 Write a program that prompts for a file name, then opens that file and reads through the file, 
and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
"""
"""
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for i in fh:
    print(i.upper().rstrip())
"""

"""
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, 
looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average 
of those values and produce an output as shown below. Do not use the sum() function or a variable named 
sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
when you are testing below enter mbox-short.txt as the file name.
"""
"""
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, 'r')
count = 0
tot = 0.0
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count = count + 1
    tot = float(line[line.find('0'):len(line)]) + tot
avg = tot / count
print("Average spam confidence:", avg)
"""

"""
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() 
method. The program should build a list of words. 
For each word on each line check to see if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
"""
"""
fname = input("Enter file name: ")
file = open(fname,'r')
wordlist = list()
for words in file:
    word = words.split()
    for i in range(len(word)):
        if(word[i] not in wordlist):
            wordlist.append(word[i])
        continue
wordlist.sort()
print(wordlist)
"""

"""
8.5 Open the file mbox-short.txt and read it line by line. 
When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line 
(i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""
'''
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
emaillist = list()
for reqword in fh:
    if not reqword.startswith('From '):
        continue
    email = reqword.split()
    count = count + 1
    print(email[1])
    emaillist.append(email[1])

print("There were", count, "lines in the file with From as the first word")

'''
'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times 
they appear in the file. After the dictionary is produced, the program reads through the dictionary using a
maximum loop to find the most prolific committer.
'''

name = 'D:\office Drive\Capgemini\learnings\Python Traning\handson\Dataset\mbox-short.txt'
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
emaildict = dict()
for line in handle:
    if not line.startswith('From:'):
        continue
    word = line.split()
    emaildict[word] = emaildict.get(word, 0) + 1 
print(emaildict)
bigcount = None
bigword = None
for (k,v) in emaildict.items():
    if bigcount is None or v > bigcount:
        bigcount = v
        bigword = k
print(bigword, bigcount)




'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of 
the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second
 time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''
'''
name = 'D:\office Drive\Capgemini\learnings\Python Traning\handson\Dataset\mbox-short.txt'
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name,'r')
hoursdict = dict()
for line in handle:
    if not line.startswith('From '):
        continue
    word = line.split()
    time = word[5]
    hours = time[:2]
    hoursdict[hours] = hoursdict.get(hours, 0) + 1
sort = sorted(hoursdict.items())
for k,v in sort:
    print(k,v)
'''