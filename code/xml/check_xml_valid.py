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
        print('����һ��������XML�ĵ�')
    except Exception:
        print ('�ⲻ��һ��������XML�ĵ�')
        # print ('����ԭ��',e)

    try:
        print("afddf")
    except:
        print("nice")
