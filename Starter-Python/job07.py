for r in range(0,101):

    if r % 3 == 0 and r % 5 == 0:
        print("FizzBuzz")
    elif r % 3 == 0:
        print("Fizz")
    elif r % 5 == 0:
        print("Buzz")
    else:
        print(r)