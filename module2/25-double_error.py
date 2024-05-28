def bad_fun(n):
    try:
        return n / 0 # raises ZeroDivisionError
    except:
        print("I did it again!")
        raise # raises ZeroDivisionError again.


try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")
