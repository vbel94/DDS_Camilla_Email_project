
import os
import sys
import Data_Controller
import camellia_tool
import String_Generation
import dss_tools
def Mail_Write(sourceMail):
    while(True):
     print('--------------------WRITE MAIL--------------------')
     Email=input("Enter the e-mail of the receiver: ")
     if(Data_Controller.MailExist(Email)==True):  
        break
     else:
         print("ERROR - THE MAIL OF THE RECEIVER DOES NOT EXIST!")
         print('--------------------------------------------------\n')
    plain=input("Enter the message you want to sent: ")
    print('--------------------------------------------------\n')
    print('~THE MESSAGE WAS CREATED~\n')
    while True:
        print('------------------MAIL DECRYPTION-----------------')
        Key=input("Enter a Key to decrypt the message with (16/24/32 Bytes): ")
        if(len(Key)==16 or len(Key)==24 or len(Key)==32):
            print('--------------------------------------------------\n')
            print('~THE MESSAGE WAS SENT~')
            break
        else: 
         print("ERROR - THE KEY MUST BE 16 OR 24 OR 32 BYTES!")
         print('--------------------------------------------------\n')
    IV=String_Generation.randomString() #generat vector IV
  
    plain=camellia_tool.encrypt(str(plain),16,Key,IV)
    public_key=Data_Controller.GetPublicKey(Email)
    plain=dss_tools.encrypt_dss(public_key,plain)
    Data_Controller.sentmails(sourceMail,Email,plain,IV)#(email_sender,email_receiver,key,mail_txt,iv):


    

    

    
    
    #Mail_Write(plain)
   