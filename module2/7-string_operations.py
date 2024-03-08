# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))


# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

#t = [0, 1, 2]
print(min(t))

for l in t:
    print(ord(l));

# tambien existe la funcion max() que es similar pero busca el valor mayor
print("---------------------------------");
#metodo index. Comienza desde el principio, buscando la primer coincidencia que se de en su argumento
# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

#metodo list
#convierte string a lista con sus caracteres individuales. Tambien convierte tuplas y diccionarios.
print(list("abcdef"));

mydick = {
    "nombre": "Diego",
    "profesion": "Ing. de Sistemas.",
    "cursos": ["CCNA1", "CCNA2", "CCNA3"]
}

print(mydick);
print(list(mydick));

# el metodo count me dice cuantas coincidencias existen del argumento en la cadena

print("Diego Herrera".count("z"));

print(list("abcd").count("a"));