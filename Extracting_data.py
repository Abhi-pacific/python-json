import urllib.request
import json
sum = 0
url = 'http://py4e-data.dr-chuck.net/comments_1738514.json'
r = urllib.request.urlopen(url).read()
with open('D:\python-json\data.json','w') as dj:
    dj.write(r.decode())

data_json = json.loads(r)

for item in data_json['comments']:
    sum += item['count']
print(sum)

