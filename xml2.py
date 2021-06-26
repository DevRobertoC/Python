# Working with XML
import xml.etree.ElementTree as ET

#String XML
input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user') # lst it's a list of trees
print('User count:', len(lst))

for item in lst: 
    print('Name', item.find('name').text) # Get text between name tags
    print('Id', item.find('id').text) # Get text between id tags
    print('Attribute', item.get('x')) # Get value of x in the tag user