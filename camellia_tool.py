import math
import camellia
import Data_Controller
#https://he.wikipedia.org/wiki/%D7%90%D7%95%D7%A4%D7%9F_%D7%94%D7%A4%D7%A2%D7%9C%D7%94_%D7%A9%D7%9C_%D7%A6%D7%95%D7%A4%D7%9F_%D7%91%D7%9C%D7%95%D7%A7%D7%99%D7%9D=iv
def encrypt(text, n,key,iv):
    thislist = []
    text=text+'#camelliaVladiDanaIdo'
    text=text+text.join([char * (n-len(text)%n) for char in '#'])
    final_txt=""
    numOfArrays = math.ceil(len(text) / n)
    for i in range(0, numOfArrays):
        thislist.append(text[i * n:n * (i + 1)])
        c1 = camellia.CamelliaCipher(key=bytes(key,encoding='latin1'), IV=bytes(iv,encoding='latin1'), mode=camellia.MODE_CBC)
        thislist[i] = c1.encrypt(bytes(thislist[i], encoding='latin1'))
       
        thislist[i]=thislist[i].decode(encoding='latin1')
        final_txt=final_txt+thislist[i]+'\n' 
    return final_txt    
  

def decrypt(text,n,key,iv):
  
  finalText=''
  text=text.split("\n")
 
  for i in range(0, len(text)-1):
    c2 = camellia.CamelliaCipher(key=bytes(key,encoding='latin1'), IV=bytes(iv,encoding='latin1'), mode=camellia.MODE_CBC)
    text[i] = c2.decrypt(bytes(text[i], encoding='latin1'))
    finalText=finalText+text[i].decode(encoding='latin1')
  word = finalText.split("#camelliaVladiDanaIdo")
  finalText=word[0]
  if(len(word)==2):
    return finalText
  else:
    None


      
    
    
     

#----test----
#thislist=encrypt("dsssssssssssssssrrrrrrrrrrrrrrr#",16,'16 byte longs keyvvvvvvvv','16 byte long key')
#dec=decrypt(thislist,16,'16 byte long key16 byte long key','16 byte long key')
#print(dec)
#mails=Data_Controller.getmails("vladi")

#mails=mails[0]['mail_txt']

#decrypt(mails,16,'16 byte long key')
#mails=mails.split(',')
#print(mails[1])