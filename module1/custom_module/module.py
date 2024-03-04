#!/usr/bin/env python3

#print("I like to be a Module.");

# cuando ejecuto este modulo directamente, el nombre de la variable __name__ es __main__
# cuando ejecuto el archivo que importa este modulo, su nombre es el nombre del archivo
#print(__name__);

""" module.py - an example of a python module """

_counter = 0; # verifica cuantas veces se ha invocado el modulo

def sum1(the_list):
    global _counter;
    _counter += 1;
    the_sum = 0;
    for elemet in the_list:
        the_sum += elemet;
    return the_sum;

def prod1(the_list):
    global _counter;
    _counter += 1;
    prod = 1;
    for element in the_list:
        prod *= element;
    return prod;

if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.");
    my_list = [i + 1 for i in range(5)];
    print(sum1(my_list) == 15);
    print(prod1(my_list) == 120);
    print(my_list);
else:
    print("I like to be a module");