'''
Created on May 6, 2020

@author: KOKULAKRISHNAN
'''
#Module - 4 Using Databases with Python
#-----------------------Chapter 14-----------------
#14.2 Our First Class and Object
'''
from Coursera_Assignments.Module_2_Assignments import name
'''
'''
class PartyAnimal:
    x = 0
    y = 1
    
    def party(self):
        self.x = self.x + 1
        print("so far", self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()
print("Type", type(an))
print("Dir", dir(an))
'''

#14.3 Object Life Cycle
'''
class PartyAnimal:
    x = 0 
    
    def __init__(self):
        print('I am constructed')
        
    def party(self):
        self.x = self.x + 1
        print('so far', self.x)
        
    def __del__(self):
        print('I am destructed', self.x)
            
an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)
'''

    #another example for multiple object instance
    
'''
In this below example we have two independent 
instances
'''
'''
class PartyAnimal:
    x = 0
    
    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")
        
    def party(self):
        self.x = self.x + 1
        print(self.name, "party Count", self.x)
        
s = PartyAnimal("sally")
s.party()

j = PartyAnimal("Jim")
j.party()
j.party()
'''

#14.4 Object inheritance
'''
In this below example,

FootballFan is a class which extends PartyAnimal. 
It has all the capabilities of PartyAnimal and 
more
'''
'''
class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, nam):
        self.name = nam
        print(self.name, "constructed")
        
    def party(self):
        self.x = self.x + 1
        print(self.name, "Party Count", self.x)
        
class FootballFan(PartyAnimal):
    points = 0 
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name,"points", self.points)
        
s = PartyAnimal("sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()
'''

# 15. Single Table CURD 
'''
we work on the "worked Example: Counting 
email in a Database"
'''
#'D:\office Drive\Capgemini\learnings\Python Traning\handson\Dataset\mbox-short.txt'
'''
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute(''''''
DROP TABLE IF EXISTS Counts'''''')

cur.execute(''''''
CREATE TABLE Counts(email TEXT, count INTEGER)'''''')

fname = input('Enter the file name: ')
if(len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count from Counts where email = ?', (email,)) #--> the email which we entered is a tuple, if we have some other values we can also mention in it
    row = cur.fetchone()
    if row is None:
        cur.execute(''''''INSERT INTO Counts (email,count) VALUES (?,1)'''''',(email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',(email,))
    conn.commit() 
    
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10' 

for row in cur.execute(sqlstr):
    print(str(row[0]),(row[1]))
    
#cur.execute(sqlstr) --> returns tuples

cur.close()      
'''      

