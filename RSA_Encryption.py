def encrypt(plaintext,public_key):
	n, key = public_key
	cipher = [chr((ord(char) ** key) % n) for char in plaintext]
	return ''.join(cipher)
