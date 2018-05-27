# get the code of a given URL as html text string
# Python3 uses urllib.request.urlopen()
# get the encoding used first
# tested with Python 3.1 with the Editra IDE

import urllib.request

def extract(text, sub1, sub2):
    """
    extract a substring from text between first
    occurances of substrings sub1 and sub2
    """
    print("sub1:", sub1)
    print("sub2:", sub2)
    print(text.split(sub1,1)[-1])
    print(text.split(sub1,1)[-1].split(sub2))
    print(text.split(sub1,1)[-1].split(sub2)[1])
    # print(text.split(sub1,1)[-1].split(sub2,2)[1]).split(sub2)

    return text.split(sub1, 1)[-1].split(sub2, 2)[1]


fp = urllib.request.urlopen("http://www.python.org")

mybytes = fp.read()
print(mybytes)

encoding = extract(str(mybytes).lower(), 'charset=', '"')
print('-'*50)
print( "Encoding type = %s" % encoding )
print('-'*50)

if encoding:
    # note that Python3 does not read the html code as string
    # but as html code bytearray, convert to string with
    mystr = mybytes.decode(encoding)
    print(mystr)
else:
    print("Encoding type not found!")


fp.close()