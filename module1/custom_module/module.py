#print("I like to be a Module.");

# cuando ejecuto este modulo directamente, el nombre de la variable __name__ es __main__
# cuando ejecuto el archivo que importa este modulo, su nombre es el nombre del archivo
#print(__name__);

if __name__ == "__main__":
    print("I prefer to be a module");
else:
    print("I like to be a module");