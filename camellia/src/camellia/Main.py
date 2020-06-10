import camellia
plain = b"dddd is a text."
c1 = camellia.CamelliaCipher(key=b'16 byte long key', IV=b'16 byte iv. abcd', mode=camellia.MODE_CBC)
encrypted = c1.encrypt(plain)
c2 = camellia.CamelliaCipher(key=b'16 byte long keyaaa', IV=b'16 byte iv. abcd', mode=camellia.MODE_CBC)
decrypted = c2.decrypt(encrypted)
print(encrypted)
print(decrypted)