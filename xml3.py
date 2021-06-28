#Working with XML and URLLIB

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

numlist = list()
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ') # input http://py4e-data.dr-chuck.net/comments_1167753.xml 
                        # or http://py4e-data.dr-chuck.net/comments_42.xml 
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieving', url)
print('Retrieved: ', len(data), 'characters') # Count characters
tree = ET.fromstring(data)
lista = tree.findall('comments/comment')
print('Count:',len(lista))

counts = tree.findall('.//count') # make a lista with the tag <count>
#print(type(counts)) - This is a list
for x in counts:
    numlist.append(int(x.text))
    
print('Sum: ', sum(numlist))