num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        sum = num1 + num2
        print("The result is ", sum)

    case "-":
        difference = num1 - num2
        print("The result is ", difference)

    case "*":
        product = num1 * num2
        print("The result is ", product)

    case "/":
        if num2 != 0:
            quotient = num1 / num2
            print("The result is ", quotient)
        else:
            print("Cannot divide by zero.")

        