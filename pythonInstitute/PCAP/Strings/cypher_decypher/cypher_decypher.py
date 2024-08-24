# Caesar cipher.
'''
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)
'''

#IPXUPFODSZQUUIJTNFTTBHF


text = input("Insert the text to decrypt: ")
decrypt = ''

for char in text:
    if not char.isalpha():
        continue
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    decrypt += chr(code)
    
print(decrypt)

