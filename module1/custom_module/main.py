from module import sum1, prod1;
# cuando python importa el modulo por primera vez, lo traduce a su forma compilada. Pero no una
# compilacion en binario como tal, sino una forma semi-compilada interna de python.
# este es el archivo que con extension pyc.

#print(_counter);

zeroes = [0 for i in range(5)];
ones = [1 for i in range(5)];

print(sum1(zeroes));
print(prod1(ones));