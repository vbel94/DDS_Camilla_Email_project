import json
def login(email,password):
  with open('./data.txt') as json_file:
    data = json.load(json_file)
    
  for d in data['data']:
    if(d["email"]==email and d["password"]==password):
     return d
    

    
