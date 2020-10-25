import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = input('Enter Link - ')
url = serviceurl
#print('Retrieving', url)
connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()

total = 0

info = json.loads(data)
#print(json.dumps(info, indent=4))
#print('User count:', len(info))

for item in info['comments']:
    hsn = int(item['count'])
    total = total + hsn
    #print('Name', item['name'])
    #print('Count', item['count'])
print('Total Sum = ', total)    