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
    else:
     return None
def sentmails(email_sender,email_receiver,key,mail_txt):
  with open('./data.json') as json_file:
    data = json.load(json_file)
    for d in data['data']:
      if(d["email"]==email_receiver):
        
        d["email_received"].append({
         "mail_txt":mail_txt,
         "key":key,
         "from":email_sender
         })
        with open("./data.json", 'w') as fp:
          json.dump(data, fp)
#mails=getmails("vladi")



