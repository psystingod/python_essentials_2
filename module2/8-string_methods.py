# Demonstrating the capitalize() method:
print('aBcD'.capitalize())
# este metodo coloca la primera letra con indice 0 en mayuscula y todo lo demas minuscula.

# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']')

# Demonstrating the endswith() method:
# verifica si una string dada termina con el argumento dado
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

# Demonstrating the find() method:
# similar al metodo index, pero este busca un substring dentro del string, en caso de no estar
# no genera error, devuelve -1. Funciona solo con strings.
print("Eta".find("ta"))
print("Eta".find("mma"))
# Si necesitamos buscar si un solo caracter existe en una cadena, no usemos find. in sera mas rapido.

# variacion de 2 parametros del metodo find.
# el argumento 2 es el indice desde el cual comenzara a realizar la busqueda.
print('kappa'.find('a', 2))

# Demonstrating the rfind() method:
# parecido a find, solo que comienza la busqueda de derecha a izquierda.
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))