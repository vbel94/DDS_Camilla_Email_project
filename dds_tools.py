
import RSA_Encryption
import RSA_Decryption
import hashlib
import key_generation
import sys
public_key1,private_key1= key_generation.generate_key()
public_key2,privte_key2= key_generation.generate_key()
def encrypt_dds(public_key,text):
    m = text
    h1 = hashlib.sha224(m.encode('latin1'))
    ct = RSA_Encryption.encrypt(h1.hexdigest(), public_key)
    final_message = m + '&' + ct
    return final_message

def decrypt_dds(privte_key,text):
    m2 = text
    m2 = text.split('&')

    pt = RSA_Decryption.decrypt(m2[1], privte_key)
    h2 = hashlib.sha224(m2[0].encode('latin1'))
    if (pt == h2.hexdigest()):
        print('The digital signature has been verified!!')
    else:
        print('Sorry, the digital signature could not be verified...')
    return m2[0]
    
    
