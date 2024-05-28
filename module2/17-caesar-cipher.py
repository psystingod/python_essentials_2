# Caesar cipher.
text = input("Enter your message: ")
cipher = ''

for ch in text:
    if not ch.isalpha():
        continue;
    
    ch = ch.upper();
    code = ord(ch) + 1;
    
    if code > ord('Z'):
        code = ord('A');
    cipher += chr(code);
    
    
print(cipher);