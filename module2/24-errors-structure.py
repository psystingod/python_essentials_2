try:
    1/0;
except BaseException:
    print("Catch it!")
except ValueError:
    print("Error");
except ArithmeticError:
    print("Zero Division");

try:
    1/0;
except (BaseException, ArithmeticError):
    print("Error");