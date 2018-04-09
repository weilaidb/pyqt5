#coding=utf-8
from xml.etree import ElementTree as ET
per=ET.parse('abc.xml')
p=per.findall('./login/item')

for oneper in p:
    for child in oneper.getchildren():
        print (child.tag,':',child.text)


p=per.findall('./item')

for oneper in p:
    for child in oneper.getchildren():
        print (child.tag,':',child.text)