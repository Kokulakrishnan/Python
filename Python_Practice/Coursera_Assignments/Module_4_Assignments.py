'''
Counting Organizations
This application will read the mailbox data (mbox.txt) and count the number of email messages per organization 
(i.e. domain name of the email address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)
When you have run the program on mbox.txt upload the resulting database file above for grading.
If you run the program multiple times in testing or with dfferent files, make sure to empty 
out the data before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.

The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.

Because the sample code is using an UPDATE statement and committing the results to the database as each record 
is read in the loop, it might take as long as a few minutes to process all the data. 
The commit insists on completely writing all the data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop. 
In any database program, there is a balance between the number of operations you execute between commits 
and the importance of not losing the results of operations that have not yet been committed.
'''
'''
from builtins import True, None
'''
'''
import urllib.request, urllib.parse, urllib.error
import sqlite3

conn = sqlite3.connect('counting_organization.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS COUNTS')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

url = 'D:\office Drive\Capgemini\learnings\Python Traning\handson\Dataset\mbox.txt'
filetext = open(url,'r')

for items in filetext:
    if not items.startswith('From '): continue
    words = items.split(' ')
    emailsplit = str(words[1]).split('@')
    print(emailsplit)
    domainname = emailsplit[1]
    cur.execute('SELECT count FROM COUNTS WHERE org = ?',(domainname,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO COUNTS (org,count) VALUES (?,1)',(domainname,))
    else:
        cur.execute('UPDATE COUNTS SET count = count + 1 WHERE org = ?',(domainname,))  
    conn.commit()
    
sqlstr = 'select org, count from COUNTS order by count DESC LIMIT 2'
for row in cur.execute(sqlstr):
    print(str(row[0]),str(row[1]))
    
cur.close()  
'''    

'''
Music Track Database

This application will read an iTunes export file in XML and produce a properly normalized database with this structure:

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);


You can use this code as a starting point for your application: 
http://www.py4e.com/code3/tracks.zip. The ZIP file contains the Library.xml 
file to be used for this assignment. You can export your own tracks from iTunes and create a database, 
but for the database that you turn in for this assignment, only use the Library.xml data that is provided.

To grade this assignment, the program will run a query like this on your uploaded database and 
look for the data it expects to see:

SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
The expected result of the modified query on your database is: (shown here as a simple HTML table with titles)


Track                                        Artist            Album            Genre
Chase the Ace                                AC/DC            Who Made Who       Rock
D.T.                                         AC/DC            Who Made Who       Rock
For Those About To Rock (We Salute You)      AC/DC            Who Made Who       Rock
'''
'''
import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('Musial_database.sqlite')
cur = conn.cursor()

cur.executescript(''''''
    
    DROP TABLE IF EXISTS Artist;
    
    DROP TABLE IF EXISTS Album;
    
    DROP TABLE IF EXISTS GENRE;
    
    DROP TABLE IF EXISTS Track;
    
    CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);  
    '''''')

fname = 'D:\office Drive\Capgemini\learnings\Python Traning\handson\Dataset\Library.xml'


def lookup(d,key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print(all)

for entry in all:
    print(entry)
    if(lookup(entry, 'Track ID') is None): continue
    name = lookup(entry, 'Name')
    artist = lookup(entry,'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry, 'Genre')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    #print(name)
    #print(artist)
    #print(album)
    #print(genre)
    #print(count)
    #print(rating)
    #print(length)
    
    if name is None or artist is None or album is None or genre is None: continue
    
    cur.execute('INSERT or IGNORE INTO Artist (name) VALUES(?)',(artist, ))
    cur.execute('INSERT or IGNORE INTO Genre (name) VALUES(?)',(genre, ))
    
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist, ))
    artist_id = cur.fetchone()[0]
    print(artist_id)
    cur.execute('INSERT or IGNORE INTO Album(artist_id, title) VALUES(?,?)',(artist_id, name))
    
    
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre, ))
    genre_id = cur.fetchone()[0]
    #print(genre_id)
    cur.execute('SELECT id FROM Album WHERE artist_id = ?', (artist_id, ))
    album_id = cur.fetchone()[0]
    
    
    cur.execute('INSERT or REPLACE INTO Track (title, album_id, genre_id, len, rating, count) VALUES(?,?,?,?,?,?)',(name, album_id, genre_id, length, rating, count))
     
    conn.commit()

print('completed')
    
'''
'''
This application will read roster data in JSON format, parse the file, and 
then produce an SQLite database that contains a User, Course, and Member table and populate the tables from the data file.

You can base your solution on this code: http://www.py4e.com/code3/roster/roster.py - this code is incomplete 
as you need to modify the program to store the role column in the Member table to complete the assignment.

Each student gets their own file for the assignment. Download this file and save it as roster_data.json. 
Move the downloaded file into the same folder as your roster.py program.

Once you have made the necessary changes to the program and it has been run successfully reading the above JSON data, 
run the following SQL command:

SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X
Find the first row in the resulting record set and enter the long string that looks like 53656C696E613333.
'''
'''
import json
import sqlite3

conn = sqlite3.connect('roster-assignment.sqlite3')
cur = conn.cursor()

cur.executescript(''''''

DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE);
CREATE TABLE Course (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT UNIQUE);
CREATE TABLE Member (user_id INTEGER, course_id INTEGER, role INTEGER, PRIMARY KEY (user_id, course_ID));

    '''''')

fname = r'D:\office Drive\Capgemini\learnings\Python Traning\handson\Dataset\roster_data.json'  

filedata = open(fname).read()
json_data = json.loads(filedata)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]
    
    
    #print((name, title))
    
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name, ))
    cur.execute('SELECT id FROM User WHERE name = ?', (name, ))
    user_id = cur.fetchone()[0]
    
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)',(title, ))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title, ))
    course_id = cur.fetchone()[0] #this returns tuple

    cur.execute('INSERT or REPLACE INTO Member (user_id, course_id, role) VALUES (?,?,?)', (user_id, course_id, role, ))
    
    conn.commit()
    
print('Completed')
'''

'''
Retrieving GEOData
Download the code from http://www.py4e.com/code3/geodata.zip - then unzip the file and 
edit where.data to add an address nearby where you live - don't reveal where you live. 
Then run the geoload.py to lookup all of the entries in where.data (including the new one) and produce the geodata.sqlite. 
Then run geodump.py to read the database and produce where.js. You can run the programs and 
then scroll back to take your screen shots when the program finishes. Then open where.html to visualize the map. 
Take screen shots as described below. Make sure that your added location shows in all three of your screen shots.

This is a relatively simple assignment. Don't take off points for little mistakes. 
If they seem to have done the assignment give them full credit. Feel free to make suggestions if there are small mistakes. 
Please keep your comments positive and useful. 
If you do not take grading seriously, the instructors may delete your response and you will lose points.
'''
'''
#geodump.py
import sqlite3
import json
import codecs

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')
fhand = codecs.open(r'D:\office Drive\Capgemini\learnings\Python Traning\handson\Dataset\where.js', 'w', "utf-8")
print('i am trying to print the location of the file', fhand)
fhand.write("myData = [\n")
count = 0
for row in cur :
    data = str(row[1].decode())
    try: js = json.loads(str(data))
    except: continue

    if not('status' in js and js['status'] == 'OK') : continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0 : continue
    where = js['results'][0]['formatted_address']
    where = where.replace("'", "")
    try :
        print(where, lat, lng)

        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")
'''

'''
#geload.py
import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open(r"D:\office Drive\Capgemini\learnings\Python Traning\handson\Dataset\where.data")
count = 0
for line in fh:
    if count > 200 :
        print('Retrieved 200 locations, restart to retrieve more')
        break

    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]
        print("Found in database ",address)
        continue
    except:
        pass

    parms = dict()
    parms["address"] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        break

    cur.execute('INSERT INTO Locations (address, geodata) VALUES ( ?, ? )', (memoryview(address.encode()), memoryview(data.encode()) ) )
    conn.commit()
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
'''
  
