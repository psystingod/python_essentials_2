line = input("Please enter a line of numbers - separated with spaces.")
strings = line.split();
total = 0;
print(strings)
try:
    for substr in strings:
        total += float(substr);
    print(f"The total is: {total}");
except:
    print(f"{substr} is not a number");