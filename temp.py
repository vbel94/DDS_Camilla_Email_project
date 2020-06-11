pu, pr = key_generation.generate_key()
	print(pu)
	ch = 0
	while(ch != 3):
		print('Welcome to RSA Approach of DSS\n')
		print('1. Send message\n')
		print('2. Receive and verify the digital signature \n')
		print('3. Exit')
		ch = int(input('Please choose one: '))
		if(ch == 1):
			m = input('Enter plain text : ')
			h1 = hashlib.sha224(m.encode('utf-8'))
			print('Applying SHA224 on plain text : ' + h1.hexdigest() + '\n')
			ct = RSA_Encryption.encrypt(h1.hexdigest(), pu)
			print('The enciphered hash is : ', ct)
			final_message = m + '#' + ct
			print('The final message being sent over is : ', final_message)
		elif(ch == 2):
			m2 = input('Enter the received message : ')
			# m2 = final_message.split('#')
			print(m2[0], '\n', m2[1])
			pt = RSA_Decryption.decrypt(m2[1], pr)
			print('Decryption on the hash is : ', pt)
			h2 = hashlib.sha224(m2[0].encode('utf-8'))
			print('SHA224 on the message received in plaintext : ' +
				  h2.hexdigest() + '\n')
			if (pt == h2.hexdigest()):
				print('The digital signature has been verified!!')
			else:
				print('Sorry, the digital signature could not be verified...')
		elif(ch == 3):
			sys.exit('Exiting.... \n')
		elif(ch == 4):
			plain ="vladi vladi 12345 vladi vladi 12345"
			c1 = camellia.CamelliaCipher(key=b'15 byte long key', IV=b'16 byte iv. abcd', mode=camellia.MODE_CBC)
			encrypted = c1.encrypt(plain)
			c2 = camellia.CamelliaCipher(key=b'15 byte long key', IV=b'16 byte iv. abcd', mode=camellia.MODE_CBC)
			decrypted = c2.decrypt(encrypted)
			print(encrypted)
			print(decrypted)		
if __name__ == '__main__':
	main()
