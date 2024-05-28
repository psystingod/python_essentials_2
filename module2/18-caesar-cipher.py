cipher = input("Enter your coded message: ");
text = "";

for ch in cipher:
    if not ch.isalpha():
        continue;

    ch = ch.upper();
    code = ord(ch) - 1;

    if code < ord('A'):
        code = ord('Z');

    text += chr(code);

print(text);