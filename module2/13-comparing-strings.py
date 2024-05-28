"""
Las trings en python pueden ser comparadas utilizando los mismos simbolos que con numeros.

    ==
    !=
    >
    >=
    <
    <=

python compara los valores de code point caracter por caracter

"""

# caso mas simple
print("alpha" == "alpha");
print("alpha" != "Alpha");

# en cadenas de diferente tamanio, si la mas pequena es identica al inicio de la mas grande,
# la mas larga es considerada mayor.
print('alpha' < 'alphabet');

# las mayusculas se consideran menores.
print('beta' > 'Beta');

"""
Estas pruebas no son siempre como esperariamos
'10' == '010'
'10' > '010'
'10' > '8'
'20' < '8'
'20' < '80'

comparar strings con numeros no es buena idea. La ultima comparacion da typeError

'10' == 10
'10' != 10
'10' == 1
'10' != 1
'10' > 1

"""