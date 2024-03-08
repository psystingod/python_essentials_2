# los strings en python son secuencias de caracteres.
# los strings no son listas, pero en ciertas maneras pueden tratarse como listas.

my_string = "Diego Herrera";

#indexacion
for l in range(len(my_string)):
    print(my_string[l], end="");

#iteracion
for l in my_string:
    print(l, end="");