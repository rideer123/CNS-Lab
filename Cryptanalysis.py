import enchant
d = enchant.Dict("en_US")

# YZAJKTZ


cipherText = input("Enter Cipher Text: ")
print('Cipher Text is "'+ cipherText+ '"')
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
actualText=''
actualKey=0
no_of_words=len(cipherText.split())
words=[]
for key in range(len(LETTERS)):
   translated = ''
   word=''
   for symbol in cipherText:
      if symbol in LETTERS:
         num = LETTERS.find(symbol)
         num = num - key
         if num < 0:
            num = num + len(LETTERS)
         translated = translated + LETTERS[num]
         word=word+LETTERS[num]
      else:
        if d.check(word):
            words.append(word)
        else:
            words.clear()
        word=''
   if d.check(word):
        words.append(word)
   if len(words)==no_of_words:
        actualText=translated
        actualKey=key
        words.clear()
print('Actual plain text is "' + actualText+ '" with key: ' + str(actualKey))