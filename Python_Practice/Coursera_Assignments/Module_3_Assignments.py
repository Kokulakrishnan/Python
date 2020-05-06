'''
Created on May 3, 2020

@author: KOKULAKRISHNAN
'''
'''
from itertools import count
'''
'''


Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. 
You will extract all the numbers in the file and compute the sum of the numbers.

Data Files
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other 
is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
Actual data: http://py4e-data.dr-chuck.net/regex_sum_472982.txt (There are 54 values and the sum ends with 128)
These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. 
Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.
'''
'''
import re
import os
tot = 0
#THIS_FOLDER = os.path.dirname(os.path.abspath('D:\office Drive\Capgemini\learnings\Python Training\handson\Dataset'))
#filelocation = os.path.join(THIS_FOLDER, 'mbox-short.txt')
name = 'D:\office Drive\Capgemini\learnings\Python Traning\handson\Dataset\words.txt'
filehand = open(name, 'r')
for line in filehand:
    x = re.findall('[0-9]+', line)
    for items in x:
        tot = tot + int(items)
print(tot)    
'''


'''
Exploring the HyperText Transport Protocol

You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.

http://data.pr4e.org/intro-short.txt
There are three ways that you might retrieve this web page and look at the response headers:

Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data.
 Make sure to change the code to retrieve the above URL - the values are different for each URL.
Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
Use the telnet program as shown in lecture to retrieve the headers and content.
Enter the header values in each of the fields below and press "Submit".
'''
'''
import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if (len(data)< 1):
        break
    print(data.decode())
mysocket.close()
'''
'''
Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to 
http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and 
parse the data, extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and 
the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_472984.html (Sum ends with 27)
You do not need to save these files to your folder since your program will read the data directly from the URL.
 Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
Data Format
The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the
 following:

<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>
You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
Look at the sample code provided. It shows how to find all of a certain kind of tag, loop through the tags 
and extract the various aspects of the tags.
'''
'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
tot = 0
url = 'http://py4e-data.dr-chuck.net/comments_472984.html'
htmlpage = urllib.request.urlopen(url).read()
soup = BeautifulSoup(htmlpage, 'html.parser')
tags = soup('span')
for tag in tags:
    tot = tot + int(tag.contents[0])
print(tot)
'''
'''
In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
scan for a tag that is in a particular position relative to the first name in the list, follow that link and 
repeat the process a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name for your testing and 
the other is the actual data you need to process for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. 
The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Tobie.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. 
The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: H
Strategy
The web pages tweak the height between the links and hide the page after a few seconds to make 
it difficult for you to do the assignment without writing a Python program. But frankly with a little effort and 
patience you can overcome these attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point. The point is to write a clever Python program to solve the program.
'''
'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

def url_findmethod (url,position,limit, count):
    urlhtmldata = urllib.request.urlopen(url).read().decode()
    soup = BeautifulSoup(urlhtmldata, 'html.parser')
    tags = soup('a')
    if(count<limit):
        count = count + 1
        splited_url = str(tags[position-1]).split('"')
        string_splitted_url = str(splited_url[1])
        url_findmethod(string_splitted_url, position, limit, count)
    else:
        onlyname = str(tags[position-1])
        name = re.split(r'[<,>]', onlyname)
        print(name[2])
    
    
    
url = input('Enter the url: ')
limit = input('enter the limit value: ')
position = input('enter the position value: ')
count = 1
url_findmethod(url,position,limit, count)
'''











    
    











'''
Extracting Data from XML

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
The program will prompt for a URL, read the XML data from that URL using urllib and 
then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and 
the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_472986.xml (Sum ends with 28)
You do not need to save these files to your folder since your program will read the data directly from the URL. 
Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
Data Format and Approach
The data consists of a number of names and comment counts in XML as follows:

<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>
You are to look through all the <comment> tags and find the <count> values sum the numbers. 
The closest sample code that shows how to parse XML is geoxml.py. 
But since the nesting of the elements in our data is different than the data we are parsing in that 
sample code you will have to make real changes to the code.
To make the code a little simpler, you can use an XPath selector string to look through the entire tree 
of XML for any tag named 'count' with the following line of code:

counts = tree.findall('.//count')
Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. 
You could also work from the top of the XML down to the comments node and then loop through the child nodes 
of the comments node.
Sample Execution

$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
Retrieved 4189 characters
Count: 50
Sum: 2...
'''
'''
import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET
tot = 0
url = 'http://py4e-data.dr-chuck.net/comments_472986.xml'
xmldata = urllib.request.urlopen(url).read()
xmltags = ET.fromstring(xmldata)
listtags = xmltags.findall('comments/comment')
for items in listtags:
    tot = tot + int(items.find('count').text)
print(tot)
'''

'''
In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. 
The program will prompt for a URL, read the JSON data from that URL using urllib and 
then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and 
enter the sum below:
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and 
the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_472987.json (Sum ends with 73)
You do not need to save these files to your folder since your program will read the data directly from the URL. 
Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
'''
'''
import urllib.request, urllib.parse, urllib.error
import json
tot = 0
url = 'http://py4e-data.dr-chuck.net/comments_472987.json'
data = urllib.request.urlopen(url).read().decode()
passingjson = json.loads(data)
for items in passingjson['comments']:
    tot = tot + int(items['count'])
print(tot)
'''
'''
Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. 
The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, 
and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a 
place as within Google Maps.
API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://py4e-data.dr-chuck.net/json?
This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often
 as you like. If you visit the URL with no parameters, you get "No address..." response.
To call the API, you need to include a key= parameter and provide the address that you are requesting as the 
address= parameter that is properly URL encoded using the urllib.parse.urlencode() function as 
shown in http://www.py4e.com/code3/geojson.py

Make sure to check that your code is using the API endpoint is as shown above. 
You will get different results from the geojson and json endpoints so make sure you are using the same end 
point as this autograder is using.

Test Data / Sample Execution

You can test to see if your program is working with a location of "South Federal University" which will have 
a place_id of "ChIJ9e_QQm0sDogRhUPatldEFxw".
'''
'''
import urllib.request,urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

address = input('enter the address: ')
key = input('enter the key: ')
parms = dict()
parms['address'] = address
parms['key'] = key

url = serviceurl + urllib.parse.urlencode(parms)

jsondata = urllib.request.urlopen(url).read().decode()
#print(jsondata)
passingjson = json.loads(jsondata)
print(passingjson['results'][0]['place_id'])
'''

