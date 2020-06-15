import sys
import Data_Controller
import camellia_tool
import dds_tools
def Mailread(mail):
    mails=Data_Controller.getmails(mail)
    i=1
    print("you have "+str(len(mails))+ " E-mail")
    for m in mails:
        print(str(i)+". "+m['from'])
        print("content:"+m['mail_txt']+"\n")
        i+=1
    while(True):
        ch=int(input("for decrypt press number E-mail or '0' to back\n"))
        if(ch==0):
            break
        else:
            j=1
            for m in mails:
                if(j==ch):
                    while(True):
                        Key=input("Please enter a key to decode \n")
                        if(len(Key)==16):
                            plain=dds_tools.decrypt_dds(Data_Controller.GetPrivateKey(mail),m['mail_txt'])
                            plain=camellia_tool.decrypt(str(plain),16,Key,m["iv"])
                            print("The decrypted text is:\n"+ plain)
                            break
                        else:
                             break
                j+=1
                      
                    
                  
    # plain=camellia_tool.encrypt(str(plain),16,IV)
    # public_key=Data_Controller.GetPublicKey(Email)
    # plain=dds_tools.encrypt_dds(public_key,plain)
    # print()