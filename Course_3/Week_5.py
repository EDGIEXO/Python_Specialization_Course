import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = input('Enter Link - ')
url = serviceurl
#print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode()
#print('Retrieved', len(data), 'characters')
#print(data.decode())

list_1 = list()

x1 = ET.fromstring(data)
cmtlst = x1.findall('.//count')#find all count tags in x1 file
#print(len(cmtlst))
for num in cmtlst:
    find_num = int(num.text)
    list_1.append(find_num)
print(sum(list_1))    