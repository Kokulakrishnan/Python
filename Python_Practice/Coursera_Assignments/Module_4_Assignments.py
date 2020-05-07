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

