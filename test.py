import sys
import json
import Data_Controller
import os
import Mail_Read
import Mail_Write
import key_generation
def main():
	clear = lambda: os.system('clear')
	ch = 0
	current_user = None
	while(1):
		if(current_user==None):
			print('--------------------------------------------------')
			print('Welcome to Email that supports DSS and Camillia')
			print('--------------------------------------------------\n')
			print('1. Login')
			print('2. Create new account')
			print('3. Exit')
			ch = int(input('\nPlease choose an action number and press ENTER: '))
			print('--------------------------------------------------\n')
			if(ch == 1):
				while(1):
					print('----------------------LOGIN-----------------------')
					email=input("Enter your Email account : ")  
					password = input("Enter your Email password : ")
					current_user = Data_Controller.login(email, password)
					if (current_user != None):
						print('--------------------------------------------------')
						print('\n~YOUR ACCOUNT WAS APPROVED~')

						break
					else:
						print("ERROR - NO USER WAS FOUND!")
						print('--------------------------------------------------\n')

			elif(ch == 2):
				while(True):
					print('----------------------CREATE NEW ACCOUNT-----------------------')
					email=input("Enter your Email account : ")  
					password = input("Enter your Email password : ")
					if(Data_Controller.MailExist(email)==False):
						public_key,private_key=key_generation.generate_key()
						Data_Controller.new_account(email,password,public_key,private_key)
						current_user = Data_Controller.login(email, password)
						print('\n~YOUR ACCOUNT WAS CREATED~')
						break
					else:
						print("ERROR - USER WITH SAME ID IS EXIST!")
			elif (ch == 3):
				sys.exit('Exiting.... \n')

			

		else:
			
			print('\n---------------------WELCOME----------------------')
			print('hey, '+current_user["email"].capitalize() + '!\n')
			print('1. Read mails')
			print('2. Write mail')
			print('3. Back to login')
			ch = int(input('\nPlease choose an action number and press ENTER: '))
			print('--------------------------------------------------\n')
			if(ch == 1):
				print('--------------------READ MAILS--------------------')
				Mail_Read.Mailread(current_user["email"])
				#raw_input('Please Enter to continue: ') 
			if(ch == 2):
				Mail_Write.Mail_Write(current_user["email"])
				#raw_input('Please Enter to continue: ')
			elif(ch==3):
				clear()
				current_user=None
if __name__ == '__main__':
    	main()