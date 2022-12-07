def generateKey(string, key):
	key = list(key)
	if len(string) == len(key):
		return(key)
	else:
		for i in range(len(string) -
					len(key)-1):
			key.append(key[i % len(key)])
	return("" . join(key))

def removeSpaces(text):
	newText = ""
	for i in text:
		if i == " ":
			continue
		else:
			newText = newText + i
	return newText

def cipherText(string, key):
	cipher_text = []
	for i in range(len(string)-1):
		x = (ord(string[i]) + ord(key[i]) - 194) % 26
		x += ord('A')
		cipher_text.append(chr(x))
	return("" . join(cipher_text))
	
def originalText(cipher_text, key):
	orig_text = []
	for i in range(len(cipher_text)):
		x = (ord(cipher_text[i]) - ord(key[i]) + 58) % 26
		x += ord('A')
		orig_text.append(chr(x))
	return("" . join(orig_text))

data = open("VigenereInput.txt", "r")
plainText = data.readline()
print('Plain text is: '+ plainText ) 
key = data.readline()
print("Key is: "+ key)
plainText=removeSpaces(plainText)
plainText=plainText.lower()
newkey = generateKey(plainText, key)
newkey=newkey.lower()
print("\nNew Key is: "+ newkey)
cipher_text = cipherText(plainText,newkey)
ex= open("output_file.txt","w")
ex.write("Cipher Text is: "+ cipher_text)

print("Ciphertext :", cipher_text)
DecryptedText=originalText(cipher_text, newkey)
ex.write("\nDecrypted Text is: "+ DecryptedText)
print("Original/Decrypted Text :",DecryptedText)
