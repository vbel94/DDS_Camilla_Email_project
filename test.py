import RSA_Encryption
import RSA_Decryption
import hashlib
import key_generation
import sys
import camellia
import json
import Data_Controller
import os
import Mail_Read
def main():
	clear = lambda: os.system('clear')
	ch = 0
	current_user = None
	while(1):
		clear()
		if(current_user==None):
			print('Welcome to Email that spourt DSS and camiila\n')
			print('1. login\n')
			print('2. Exit')
			ch = int(input('Please choose one: '))
			if(ch == 1):
				while(1):
					email=raw_input("Enter your Email account : ")
					password = raw_input("Enter your Email password : ")
					current_user = Data_Controller.login(email, password)
					if (current_user != None):
						break
					else:
						print("no user like that")
			elif (ch == 3):
				print(1)
			elif(ch == 2):
				sys.exit('Exiting.... \n')
		else:
			print('hey'+current_user["email"])
			print('1. read mails\n')
			print('1. write mail\n')
			print('3. back to login')
			ch = int(input('Please choose one: '))
			if(ch == 1):
				print("read mails")
				Mail_Read.Mailread(current_user["email"])
				input('Please Enter to continue: ')
			if(ch == 2):
				print("write mail")
				#writemail()
			elif(ch==3):
				clear()
				current_user=None
if __name__ == '__main__':
    	main()