def q1():
    while True:
        try:
            number = int(input("Enter an integer: "))
            print("You entered:",number)
            break
        except ValueError:
            print("Error:Please enter a valid integer.")

q1()