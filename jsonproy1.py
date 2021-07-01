import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

lista = list()
url = input('Enter location: ') # input http://py4e-data.dr-chuck.net/comments_42.json
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieving: ', url)
print('Retrieved: ', len(data), 'characters')

info = json.loads(data)
cant = len(info['comments'])
print('Count: ', cant)
#print(info['comments'][1]['count'])
#print(json.dumps(info, indent=4))

for x in range(cant):    
    lista.append(int(info['comments'][x]['count']))   
print('Sum: ',sum(lista))