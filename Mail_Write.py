
import os
import sys
import Data_Controller
import camellia_tool
import String_Generation
import dds_tools
def Mail_Write(sourceMail):
    while(True):
     Email=input("Enter Email account that you want sent a e-mail: \n")
     if(Data_Controller.MailExist(Email)==True):  
        break
     else:
         print("Mail dont Exist\n")
    plain=input("Enter Text you want to sent \n")
    while True:
        Key=input("Enter Key 16,32 Byte\n")
        if(len(Key)==16 or len(Key)==32):
            break
        else:
         print("Key must be 16,or 32 Byte Try agin\n")
    IV=String_Generation.randomString() #generat vector IV
  
    plain=camellia_tool.encrypt(str(plain),16,Key,IV)
    public_key=Data_Controller.GetPublicKey(Email)
    plain=dds_tools.encrypt_dds(public_key,plain)
    Data_Controller.sentmails(sourceMail,Email,plain,IV)#(email_sender,email_receiver,key,mail_txt,iv):


    

    

    
    
    #Mail_Write(plain)
   