#encoding=gbk
from xml.etree import ElementTree as ET

xmllist = [
    'test.xml',
    'bad.xml'
]
for xml in xmllist:
    print("%s test xml name:%s " % ('=' * 3 ,xml))
    try:
        ET.parse(xml)
        print('这是一个良构的XML文档')
    except Exception:
        print ('这不是一个良构的XML文档')
        # print ('可能原因：',e)

    try:
        print("afddf")
    except:
        print("nice")
