'''
Created on May 6, 2020

@author: KOKULAKRISHNAN
'''
#Module - 4 Using Databases with Python
#-----------------------Chapter 14-----------------
#14.2 Our First Class and Object
'''
from builtins import True, None
'''
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
'''
#worked example: Track.py (Chapter 15)
import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()
    #make some fresh tables using exeuctescript()
''''''
the difference between execute and executescript in python
execute - runs only one statement once
executescript - runs multiple statements once
''''''
cur.executescript(''''''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
CREATE TABLE Album (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, artist_id INTEGER, title TEXT UNIQUE);
CREATE TABLE Track (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE, album_id INTEGER, len INTEGER, rating INTEGER, count INTEGER);
'''''')


fname = 'D:\office Drive\Capgemini\learnings\Python Traning\handson\Dataset\Library.xml'
if(len(fname)< 1): fname = 'Library.xml'

    #method for reading the xml
def lookup(d,key):
    found = False
    for child in d:
        print('Child inside function lookup',child.text)
        if found : return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict Count:', len(all))
for entry in all:
    print('Inside for loop main method',entry)
    if(lookup(entry, 'Track ID') is None): continue
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry,'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    
    if name is None or artist is None or album is None:
        continue
    
    #print(name, artist, album, count, rating, length)
    
    cur.execute('INSERT or IGNORE INTO Artist (name) VALUES(?)',(artist, ))
    cur.execute('SELECT id FROM Artist WHERE name = ?',(artist, ))
    artist_id = cur.fetchone()[0]
    
    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?,?)',(album,artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album, ))
    album_id = cur.fetchone()[0]
    
    cur.execute('INSERT or REPLACE INTO Track (title, album_id, len, rating, count) VALUES (?, ?, ?, ?, ?)',(name, album_id, length, rating, count))
    
    conn.commit()
'''    
    
    #15.8 Many to Many Relationships
    
'''
Now an example code --> roster.py
The learning objective of this part is to know 
how to handle many to many relationships using python.
'''
'''
import json
import sqlite3


conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript(''''''

DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
CREATE TABLE Course (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE);
CREATE TABLE Member (user_id INTEGER, course_id INTEGER, role INTEGER, PRIMARY KEY (user_id, course_ID));

    '''''')


fname = r'D:\office Drive\Capgemini\learnings\Python Traning\handson\Dataset\roster_data_sample.json'
#print(fname)
str_data = open(fname).read()
#print('str_data', str_data)
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    
    
    #print((name, title))
    
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name, ))
    cur.execute('SELECT id FROM User WHERE name = ?', (name, ))
    user_id = cur.fetchone()[0]
    
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)',(title, ))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title, ))
    course_id = cur.fetchone()[0] #this returns tuple

    cur.execute('INSERT or REPLACE INTO Member (user_id, course_id) VALUES (?,?)', (user_id, course_id, ))
    
    conn.commit()
    
print('Completed')
'''

    
    