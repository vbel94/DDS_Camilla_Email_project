import sys
import Data_Controller
import camellia_tool
import dss_tools
def Mailread(mail):
    mails=Data_Controller.getmails(mail)
    i=1
    print("You have "+str(len(mails))+ " E-mails.\n")
    for m in mails:
        print("******************#" + str(i) + " MESSAGE******************");
        print("From: "+m['from'])
        print("Content:\n"+m['mail_txt'])
        print("******************#" + str(i) + " MESSAGE******************\n");
        i+=1
    while(True):
        ch=int(input("\nFor decryption enter the number of the E-mail or '0' to return and press ENTER: "))
        if(ch==0):
            print('--------------------------------------------------')
            break
        else:
            j=1
            for m in mails:
                if(j==ch):
                    while(True):
                        print('\n--------------------DECODE KEY--------------------')
                        Key=input("Please enter a key to decode message #" + str(ch) + ": ")
                        if(len(Key)==16 or len(Key)==24 or len(Key)==32):
                            plain=dss_tools.decrypt_dss(Data_Controller.GetPrivateKey(mail),m['mail_txt'])
                            print(str(plain))
                            plain=camellia_tool.decrypt(str(plain),16,Key,m["iv"])
                            if(plain==None):
                                print('\n-----------------DECODED MESSAGE------------------')
                                print('ERROR - WORNG KE')
                                print('--------------------------------------------------')
                            else:
                                print('\n-----------------DECODED MESSAGE------------------')
                                print("The decrypted text of message #" + str(ch) + " is:\n"+ plain)
                                print('--------------------------------------------------')
                            break
                        else:
                            print('ERROR - THE KEY MUST BE 16 OR 24 OR 32 BYTES!!')
                            print('--------------------------------------------------\n')
                            break
                j+=1
                      
                    
                  
#test
#Mailread("vladi3")