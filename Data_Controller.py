import json

def login(email,password):
  with open('./data.json') as json_file:
    data = json.load(json_file)
  for d in data['data']:
    if(d["email"]==email and d["password"]==password):
     return d
  return None
def getmails(email):
  with open('./data.json') as json_file:
    data = json.load(json_file)
  for d in data['data']:
    if(d["email"]==email):
     return d["email_received"]
  return None
def new_account(email,password,public_key,private_key):
  with open('./data.json') as json_file:
    data = json.load(json_file)
    data['data'].append({
      "public_key": public_key,
      "private_key": private_key,
      "email_received": [
      ],
      "id": len(data['data'])+1,
      "password": password,
      "email": email
    })
  with open("./data.json", 'w') as fp:
    json.dump(data, fp)
def sentmails(email_sender,email_receiver,mail_txt,iv):
  with open('./data.json') as json_file:
    data = json.load(json_file)
    for d in data['data']:
      if(d["email"]==email_receiver):
        
        d["email_received"].append({
         "mail_txt":mail_txt,
         "from":email_sender,
         "iv":iv
         })
      with open("./data.json", 'w') as fp:
        json.dump(data, fp)
#mails=getmails("vladi")
def MailExist(email):
  with open('./data.json') as json_file:
    data = json.load(json_file)
  for d in data['data']:
    if(d["email"]==email):
     return True
  return False

def GetPublicKey(email):
  with open('./data.json') as json_file:
    data = json.load(json_file)
  for d in data['data']:
    if(d["email"]==email):
     return tuple(map(int, d["public_key"].split(', ')))
  return None
def GetPrivateKey(email):
  with open('./data.json') as json_file:
    data = json.load(json_file)
  for d in data['data']:
    if(d["email"]==email):
      return tuple(map(int, d["private_key"].split(', ')))
  return False


#test
#new account
#new_account("vladi3","vladi3")