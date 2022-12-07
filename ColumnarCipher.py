import math

def removeSpaces(text):
	newText = ""
	for i in text:
		if i == " ":
			continue
		else:
			newText = newText + i
	return newText

def encryptMessage(plainText):
	cipher = ""
	k_indx = 0
	plainText_len = float(len(plainText))
	plainText_lst = list(plainText)
	key_lst = sorted(list(key))
	col = len(key)
	row = int(math.ceil(plainText_len / col))
	fill_null = int((row * col) - plainText_len)
	plainText_lst.extend('x' * fill_null)

	matrix = [plainText_lst[i: i + col]
			for i in range(0, len(plainText_lst), col)]
	for _ in range(col):
		curr_idx = key.index(key_lst[k_indx])
		cipher += ''.join([row[curr_idx]
						for row in matrix])
		k_indx += 1
	return cipher

def decryptMessage(cipher):
	plainText = ""
	k_indx = 0
	plainText_indx = 0
	plainText_len = float(len(cipher))
	plainText_lst = list(cipher)
	col = len(key)
	row = int(math.ceil(plainText_len / col))
	key_lst = sorted(list(key))
	dec_cipher = []
	for _ in range(row):
		dec_cipher += [[None] * col]
	for _ in range(col):
		curr_idx = key.index(key_lst[k_indx])
		for j in range(row):
			dec_cipher[j][curr_idx] = plainText_lst[plainText_indx]
			plainText_indx += 1
		k_indx += 1
	try:
		plainText = ''.join(sum(dec_cipher, []))
	except TypeError:
		raise TypeError("This program cannot",
						"handle repeating words.")
	null_count = plainText.count('_')
	if null_count > 0:
		return plainText[: -null_count]
	return plainText

data = open("ColumnarInput.txt", "r")
plainText = data.readline()
print('Plain text is: '+ plainText )
key = data.readline()
plainText=plainText[:len(plainText)-1]
print("Given Key is: ", key)
plainText=removeSpaces(plainText)
print()
cipher = encryptMessage(plainText)
print("Encrypted Message: {}".
			format(cipher))
DecryptedText=format(decryptMessage(cipher))
DecryptedText=DecryptedText[:len(plainText)]
print("Decryped Message: "+DecryptedText)
ex= open("output_file.txt","w")
ex.write("Cipher Text is: "+ cipher)
ex.write("\nDecrypted Text is: "+ DecryptedText)
