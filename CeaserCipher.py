def encrypt(plainText,key):
    result = ""
    for i in range(len(plainText)):
        char = plainText[i]
        if char == ' ':
            result += ''
        elif char.isupper():
            result += chr((ord(char) + key-65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 65)
    return result

def decrypt(cipherText,key):
    result = ""
    for i in range(len(cipherText)-1):
        char = cipherText[i]
        if char == ' ':
            result += ''
        elif char.isupper():
            result += chr((ord(char) - key-65) % 26 + 65)
    return result

print("Enter Method To give input\n1.Using File Handling\n2.Using Commad Line\n(1/2): ")
opt = int(input())
if opt==1:
    data = open("CaesarCipherInput.txt", "r")
    plainText = data.readline()
    print('Plain text is: '+ plainText )
    key = int(data.readline())
    ex= open("output_file.txt","w")
    cipherText=encrypt(plainText,key)
    ex.write('Cipher text is: '+ cipherText)
    print('Cipher text is "'+ cipherText+'"')
    decryptedText=decrypt(cipherText,key)

elif opt==2:
    plainText  = input("Enter Plain Text:  ")
    print('Plain text is: '+ plainText )
    key = int(input("Enter Key:  "))
    print('Cipher text is "'+ encrypt(plainText , key)+'"')