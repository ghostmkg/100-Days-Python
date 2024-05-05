for i in range(1, 101):
    
    if i % 3 == 0:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fuzz")
    elif i % 5 == 0:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print("Buzz")
    else:
        print(i)