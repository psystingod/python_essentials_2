# la funcion dir() hace algo similar que mostrar todo el contenido de un directorio, pero en este caso, de un paquete.
# tiene una condicion: el modulo debe ser importado como un todo, no en parte.

import math;

print(dir(math));

# si se importa con un alias, debe utilizar el alias.

# es posible tambien recorrer las entidades.
for name in dir(math):
    print(name, end="\t");

# el modulo math tiene funciones sin, cos, tan, asin, acos, atan, con las cuales hay que tener cuidado ya que trabajan con radianes.
# para manejar eso, el modulo math viene con funciones para conversion pi, radians(x), degrees(x).
# asi mismo tien esus analogos hiberbolicos.

ad = 90;
ar = math.radians(ad);
ad = math.degrees(ar);

print(ad, ar);

print(ad == 90.)
print(ar == math.pi / 2.)
print(math.sin(ar) / math.cos(ar) == math.tan(ar))
print(math.asin(math.sin(ar)) == ar)
