
choosing = True
while choosing:

    num1 = int(input("Choose a number:"))
    num2 = int(input("Choose another one:"))
    oper = input(
            "Choose an operation:\n    Options are: +, -, * or /.\n    Write 'exit' to finish.\n")

    if oper == "+":
        print("Result:", num1 + num2)
    elif oper == "-":
        print("Result:", num1 - num2)
    elif oper == "*":
        print("Result:", num1 * num2)
    elif oper == "/":
        if num2 == 0:
            print("You can't divide by zero.")
            num3 = int(input("Choose another one:"))
            print("Result:", num1 / num3)
        else:
            print("Result:", num1 / num2)
    elif oper == "exit":
        print("OK, bye bye!")
        choosing = False
        



