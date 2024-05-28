def read_int(prompt, min, max):
    try:
        val = int(input(prompt));
        if val not in range(min, max + 1):
            raise IndexError
        return val
    except ValueError:
        print("Error: wrong input");
        read_int(prompt, min, max)
    except IndexError:
        print(f"Error: the value is not within permitted range ({min}..{max})");
        read_int(prompt, min, max)


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)