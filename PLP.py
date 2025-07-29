def simple_calculator():
    print("Simple Calculator")

    print("Please enter two numbers and the operation you want to perform.")

    # Get user input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ").strip()
        
    # Perform calculation
    if operation == '+':
            result = num1 + num2
    elif operation == '-':
            result = num1 - num2
    elif operation == '*':
            result = num1 * num2
    elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
    else:
            print("Error: Invalid operation. Please use +, -, *, or /.")
            return
        
    # Display result
    print(f"Result: {num1} {operation} {num2} = {result}")

simple_calculator()