# las operaciones de conversion de numeros a strings puede llegar a ser necesarias.
# utilizamos la funcion str()

fl = 15.56;
it = 70;

print(str(fl) + str(it));

# la operacion contraria tambien es posible. Siempre y cuando la cadena sea un numero valido.
# caso contrario mostrara un ValueError.

si = "13";
sl = "13.3";

print(int(si) + float(sl));

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
s3 = sorted(s2)
print(s3[0])
print(s3[1])

s1 = '12.8'
i = int(s1) # Value error