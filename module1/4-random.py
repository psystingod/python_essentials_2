from random import random, seed, randrange, randint;
#seed(0);
for i in range(0, 4):
    print(random());

for i in range(100):
    if randrange(1,5 + 1) == 5:
        print("funcionamiento esperado", end=str(i)+"\n");
        break;
    else:
        print("Parece que no toma el extremo superior", end=str(i)+"\n");

for i in range(5):
    print(randint(1,5));
