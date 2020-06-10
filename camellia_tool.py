import math
import camellia
def encrypt(text, n,key):
    thislist = []
    text=text+'#camelliaVladiDanaIdo'
    text=text+text.join([char * (n-len(text)%n) for char in '#'])
  #  print(text)
    numOfArrays = math.ceil(len(text) / n)
    finalTxt=""
    for i in range(0, numOfArrays):
        thislist.append(text[i * n:n * (i + 1)])
        c1 = camellia.CamelliaCipher(key=bytes(key,encoding='utf8'), IV=b'16 byte iv. abcd', mode=camellia.MODE_CBC)
        thislist[i] = c1.encrypt(bytes(str(thislist[i]), encoding='utf8'))       
    return thislist    

def decrypt(text,n,key):
  finalText=''
  for i in range(0, len(text)):
    c2 = camellia.CamelliaCipher(key=b'16 byte long key', IV=b'16 byte iv. abcd', mode=camellia.MODE_CBC)
    text[i] = c2.decrypt(text[i])
    finalText=finalText+text[i].decode('utf-8')
  word = finalText.split("#camelliaVladiDanaIdo")
  finalText=word[0]
  print(finalText)  


thislist=encrypt("dsssssssssssssssrrrrrrrrrrrrrrr#",16,'16 byte long key')
decrypt(thislist,16,'16 byte long key')