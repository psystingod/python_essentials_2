the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)

print(the_text[198], the_text[199],the_text[200]);

# variante de find con 3 argumentos. El tercer argumento apunta al indice al cual no se tomara en
# consideracion en la busqueda.

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

# Demonstrating the isalnum() method:
# retornara falso solo cuando encuentre algun caracter que no sea alfanumerico.
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

# Example 1: Demonstrating the isapha() method:
# solamente lanza true si solo son caracteres
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Example 2: Demonstrating the isdigit() method:
#solamente lanza true si son digitos.
print('2018'.isdigit())
print("Year2019".isdigit())

# Example 1: Demonstrating the islower() method:
# lanza true solo si todo es minuscula
print("Moooo".islower())
print('moooo'.islower())

# Example 2: Demonstrating the isspace() method:
# lanza true si solo hay espacios
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Example 3: Demonstrating the isupper() method:
# lanza true si todo es mayuscula
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())