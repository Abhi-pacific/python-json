import json
data = '''
    {
        "name":"Abhishek",
        "phone":{"type":"intl","number":"+917302000000"},
        "email":{
        "hide":"yes"
        }
    }
'''
info = json.loads(data)
print('Name :',info["name"])