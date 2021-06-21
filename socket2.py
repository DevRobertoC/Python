#Extract data from a web page

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
print(fhand)
print("-------")
for line in fhand:
    print(line.decode().strip())

# Find numerical expression of ascii code
x = ord('i')
print(x)