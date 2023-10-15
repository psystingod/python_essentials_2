# traemos del modulo random, dos funciones que nos serviran para elegir un numero aleatorio de una secuencia de numeros.

from random import choice, sample;

my_list = [1,2,3,4,5,6,7,8,9,10];

print(choice(my_list));
print(sample(my_list, 5));
print(sample(my_list,10));


