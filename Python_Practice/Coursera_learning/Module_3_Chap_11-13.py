'''
Created on May 3, 2020

@author: KOKULAKRISHNAN
'''
'''
from builtins import None
from pip._vendor import urllib3
'''
'''
from _ast import Is
from platform import processor
from tkinter.ttk import _format_layoutlist
from pip._vendor.pyparsing import stringStart
import string
from test.test_zipfile import Tellable
from pip._vendor.distlib.util import extract_by_key
from pickle import UNICODE
from aifc import data
from bs4.builder import XML
'''

#------------------11.1 Regular Expressions--------------------

'''
In computing, a regular expression, also referred to assert
"regex" or "regexp", provides a concise and flexible means
for matching strings of text, such as particular charcters, 
words, or patters of characters. A regular expression Is
written in a formal language that can be interpreted by a 
regular expression processor
'''

#The regular expression module

'''
before you can use regular expression in your program, you
must import the library using "import re"

you can use re.search() to see if a string matches a
regular expression, similar to using the find() method
for stringStart

you can use re.findall() to extract portions of string
that match your regular expression, similar to a
combination of find() and slicing: var[5:10]
'''

#using re.search() like find()
#using re.search() like startswith()
'''
import re
hand = open('D:\office Drive\Capgemini\learnings\Python Traning\handson\Dataset\mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)
'''

#wild card characters
'''
The dot character matches any character
if you add the asterisk character, the character is 
"any number of times"
'''

#---------11.2 Extracting Data------------------------

#Matching and Extracting Data

'''
re.search() returns a True / False depending on whether
the string matches the regular expression

if we actually want the matching strings to be extracted
use the fucntion 're.findall()'
'''
'''
import re
x = 'my 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
'''

#Warning: Greedy matching 

'''
The repeat characters (* and +) push outward in both
directions (greedy) to match the largest possible string
'''
'''
import re
x = 'From: using the : character'
y = re.findall('^F.+:', x)
print(y)
'''

#Non Greedy Matching

'''
Not all regular expression repeat codes are greedy 
if you add a '?' and '*' chill out a bit...
'''
'''
import re
x = 'From: using the : character'
y = re.findall('^F.+?:', x)
print(y)
'''

#Fine - tuning string extraction

'''
you can refine the match for re.findall() and separately
determine which portion of match is to be extracted by 
using parentheses
'''
'''
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y)
'''

#another example

'''
Parentheses are not part of the match - but they Tellable
where to start and stop what string to extract
'''
'''
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('^From (\S+@\S+)', x)
print(y)
'''

#the regex expression to retrieve the domain name from email address
'''
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@\S+', lin)
print(y)
'''

#Spam confidence
'''
import re
hand = open('D:\office Drive\Capgemini\learnings\Python Traning\handson\Dataset\mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: (0.[0-9]+)', line)
    #also try ([0-9.]+)
    print(stuff)
    if len(stuff)!= 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print(numlist)
print('Maximum:', max(numlist))
'''

#Escape character

'''
if you want a special regular expression character to 
just behave normally (most of the time) you can prefix
it with '\'
'''
'''
import re
x = 'we just received $10.00 for cookies'
y = re.findall('\S[0-9.]+', x)
#we can also try ('\$[0-9.]+')
print(y)
'''

#----------------12. Network Topology-------------------------

#sockets in Python
'''
import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))
'''

#An Http request in python
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

#12.3 Unicode characters and Strings
'''
here we saw differences between python 2 and 3. 
In python three everthing is considered as UNICODE

both regular string and UNICODE are same but byte string
is different in python 3
'''

#12.4 using urlib in python
'''
since HTTP is so common, we have a library that does all 
the socket work for us and makes web pages look like a 
file
'''
'''
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
'''
'''
#handling webpage like a file 

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts= dict()

for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
'''
    
#12.5 parsing web pages

'''
web scraping
when a program or script pretends to be a browser and 
retrieves web pages, looks at those web pages, extracts information
and then looks at more web pages

search engines scrape web pages- we call this
"spidering the web" or "web crawling"
'''
#parsing data from HTML tags

''' 
we can achieve this by using beautifulSoup 
'''
'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://www.dr-chuck.com/page2.htm'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
print(tags)
for tag in tags:
    print(tag.get('href', None))

'''

#----------------13 Data on the web------------------

#13. 1Data on the web

'''
with the HTTP request/response well understood and well
supported, there was a natural move towards exchanging
data between programs using these protocols

we need to come up with an agreed way to represent data going 
between applications and across networks

There are two commonly used formats:
xml and JSON
'''

#13.2 eXtensible Markup Language
'''
here we learnt all about the xmlschema and xmltags 

and how to retrieve values from the xml data
'''

#13.3 XML Schema

'''
Describing a "Contract" as to what is acceptable XML

Description of the legal format of an XML document

expresed in terms of constraints on the structure and 
content of documents

often used to specify a "Contract" between systems -
"my systems will only accept xml that conforms to this
particular schema

if a particular piece of XML meets the specification
of the schema - it is said to validate
'''

#13.4 Parsing XML

'''
to parse xml files you need the following library to 
be included 

'import xml.etree.ElementTree as ET'
'''
'''
import xml.etree.ElementTree as ET
data = ''''''<person>
<name>chuck</name>
<phone type = "intl">
+1 734 303 4456
</phone>
<email hide = "yes"/>
</person>''''''
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
'''

#another example
'''
this example helps you in case of nested xml statements
'''
'''
import xml.etree.ElementTree as ET
input = ''''''<stuff>
    <users>
        <user x = "2">
            <id>001</id>
            <name>chuck</name>
        </user>
        <user x = "7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>''''''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print(lst)
#print('user count:', len(lst))
for item in lst:
    print('Name:', item.find('name').text)
    print('ID:', item.find('id').text)
    print('Attributes:', item.get('x'))
'''

#------------------------Chapter 13 JSON----------------

#13.5 Javascript Object Notation (JSON)
'''
import json
    #the data variable holds the triple quoted string
data = ''''''{ 
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}''''''

    #json.load retruns an object in python dictionary
info = json.loads(data)

print(info)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
print('Phone Number:', info["phone"]["number"])
'''
    #Another example for list of python dictionary 
'''    
import json
#input = ''''''[{"id" : "001","x" : "2","name" : "chuck"},{"id" : "009","x" : "7", "name" : "chuck"}]''''''
     #info returns a list here since the data inside the input is the list containing two dictionaries
info = json.loads(input)
print('user count:', len(info))
for item in info:
    print('Name:',item['name'])
    print('id:', item['id'])
    print('Attribute', item['x'])
'''

#13.6 Service Oriented Approach
'''
i took some notes in the notepad++ read there
'''
    
#13.7 Using application programming interfaces

'''
here i develop a code in python to connect the google map
API's to retrieve some data from google maps
'''
'''
import urllib.request, urllib.parse, urllib.error
import json

servicour1 = 'http://maps.googleapis.com/maps/api/gecode/json?'

while True:
    address = input('Enter Location: ')
    api_key = input('Enter the API key: ')
    if len(address) < 1: break
    
    parms = dict()
    parms['address'] = address
    parms['key'] = api_key 
    
    url = service1 + urllib.parse.urlencode(parms)
    
    print('Retrieving', url)
    
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    
    try:
        js = json.loads(data)
    except:
        js = None
        
    if not js or 'status' not in js or js['status'] != 'OK': 
        print('===failure to retrieve ========')
        print(data)
        continue
    
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
'''

#13.8 Securing API requests

    #Twitter API's connectivity to retrieve data 
'''  
import urllib.request, urllib.parse, urllib.error
import oauth
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

consumer_key = ''
consumer_secret = ''

token_key = ''
token_secret = ''

def augment(url, parameter):
    secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer(secrets['consumer_key'], secrets['consumer_scret'])
    token = oauth.OAuthToken(secrets['token_key'], secrets['token_secret'])
    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer, token = token, http_method = 'GET', http_url = url, parameters = parameters)
    oauth_request.sign_request(oauth.OAuthSingatureMethod_HMAC_SHA1(),consumer, token)
    return oauth_request.to_url()
 
while True:
    print('')
    acct = input('Enter twitter account:')
    if (len(acct) < 1): break
    
    url = augment(TWITTER_URL,{'screen_name':acct, 'count' : '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    print(json.dump(js, indent = 4))
    
    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print(' ', s[:50])
    
'''   