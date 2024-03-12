# Demonstrating the join() method:
# recibe como argumento una lista, que debe ser solo de strings. Las une con el separador del
# que llama al metodo.
print(",".join(["omicron", "pi", "rho"]))

# Demonstrating the lower() method:
# convierte todo a minuscula
print("SiGmA=60".lower())

# Demonstrating the lstrip() method:
# la version sin argumentos elimina todos los espacios en blanco del lado mas a la izquierda.
# la version con un argumento elimina todos los caracteres listados en el argumento.

print("[" + " tau ".lstrip() + "]")

print("www.cisco.com".lstrip("w."))

print("pythoninstitute.org".lstrip(".org"))

# Demonstrating the replace() method:
# Todas las coincidencias del primer argumento se reemplazan con el seundo.
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

print("www.netacad.com".replace("", "pythoninstitute.org"))
# con tres argumentos, puedo limitar el numero de reemplazos, de izq a der
print("Apple".replace("", "Grape", 2))