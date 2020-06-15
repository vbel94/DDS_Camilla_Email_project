import RSA_Encryption
import RSA_Decryption
import hashlib
import key_generation
import sys
import camellia
import Data_Controller
def Mailread(mail):
    mails=Data_Controller.getmails(mail)
    print(mails[0])

Mailread("vladi")