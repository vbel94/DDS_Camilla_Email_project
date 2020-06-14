import math
import camellia
import Data_Controller
def encrypt(text, n,key):
    thislist = []
    text=text+'#camelliaVladiDanaIdo'
    text=text+text.join([char * (n-len(text)%n) for char in '#'])
    final_txt=""
    numOfArrays = math.ceil(len(text) / n)
    for i in range(0, numOfArrays):
        thislist.append(text[i * n:n * (i + 1)])
        c1 = camellia.CamelliaCipher(key=bytes(key,encoding='utf8'), IV=b'16 byte iv. abcd', mode=camellia.MODE_CBC)
        thislist[i] = c1.encrypt(bytes(thislist[i], encoding='utf8')) 
        
        thislist[i]=str(thislist[i])
        final_txt=final_txt+thislist[i]+'\n' 
    return final_txt    
  

def decrypt(text,n,key):
  
  finalText=''
  text=text.split("\n")
 
  for i in range(0, len(text)-1):
    print(text[i])
  
      
    
    
     


thislist=encrypt("dsssssssssssssssrrrrrrrrrrrrrrr#",16,'16 byte long key')
#decrypt(thislist,16,'16 byte long key')
#Data_Controller.sentmails("vladi","vladi",'16 byte long key',str(thislist))
#mails=Data_Controller.getmails("vladi")
#mails=mails[0]['mail_txt']
#mails=mails.split(',')
#print(mails[1])