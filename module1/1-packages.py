# importar paquetes en python
# la manera mas simple de importar un modulo es importar todo el modulo, en este caso math.

import math;

# podemos importar modulos diferentes de la misma manera, en una linea separada, o asi: import mod1, mod2;
print(math.pi);
print(math.sin(math.pi/2));

# en este caso math (y los modulos) representan el namespace.
# podemos realizar una implementacion propia y observar que nuestra implementacion de sin puede coexistir con el namespace math.
# --------------------------------------------------------------------------
def sin(x):
    if 2 * x == pi:
        return 0.99999999;
    else:
        return None;

pi = 3.14;

print(sin(pi/2));
print(math.sin(math.pi/2));

# existe la definicion no calificada. Esn este caso, dependiente el orden en el que importemos, reemplazara nuestra definicion o la importada.
#----------------------------------------------------------------------------
from math import pi;
# --------------------------------------------------------------------------

# podemos importar tambien todos los modulos con from module import *. Hay que evitarla a menos que conozcamos lo que hacemo.
# es muy probable que no podamos manejar los conflictos de nombres.

# otra manera que tenmos para importar y que puede ayudarnos con los conflictos de nombres es la siguiente

import math as mathe;
from math import sin as sen;

from math import pi as p, sin as sen, cos as cs;

# analiza las diversas formas que tenemos para importar modulos.
