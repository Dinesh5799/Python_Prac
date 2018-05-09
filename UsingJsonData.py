import json

data = '''{
  "name" : "Dinesh Kumar",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)

print("Name: ",info['name'])
print("Email Status Hidden: ",info['email']['hide'])