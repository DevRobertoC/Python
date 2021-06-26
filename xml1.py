#Working with XML

import xml.etree.ElementTree as ET

# Strin XMl 
data = '''
    <person>  
        <name>Chuck</name>
        <phone type="intl">
            +1 734 303 4456
        </phone>
        <email hide="yes"/>
    </person>'''
 # The triple quote ''' means multiline string

#Find tag in XML
tree = ET.fromstring(data)
print('Name:', tree.find('name').text) #With .text you get Chuck
print('Attr:', tree.find('email').get('hide')) # get yes of email tag