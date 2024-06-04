def main():
    print("Simple Calculator")
    while True:
        num1 = float(input("Enter first number"))
        num2 = float(input("Enter second number"))
        operation = input("Enter an operation (+,-,*,/) or q to quit \n")

        match operation:
            case "+":
               result = add(num1, num2)
            case "-":
                result = sub(num1, num2)
            case "*":
                result = mul(num1, num2)
            case "/":
                result = div(num1, num2)
            case "q":
                break
            case default:
                print("Invalid Operation")
                break
        print(f"The result of {num1} {operation} {num2} is: {result}") 
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."
if __name__ == "__main__":
    main()