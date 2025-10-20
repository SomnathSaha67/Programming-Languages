operator = input("Enter operator (+, -, *, /): ")
n = int(input("Enter number of operands: "))
if n <= 0:
    print("Number of operands must be >= 1")
if operator == "+":
    total = 0.0
    for i in range(n):
        total += float(input(f"Enter operand {i+1}: "))
    print(total)
elif operator == "-":
    result = float(input("Enter operand 1: "))
    for i in range(2, n+1):
        result -= float(input(f"Enter operand {i}: "))
    print(result)
elif operator == "*":
    result = 1.0
    for i in range(n):
        result *= float(input(f"Enter operand {i+1}: "))
    print(result)
elif operator == "/":
    result = float(input("Enter operand 1: "))
    for i in range(2, n+1):
        denom = float(input(f"Enter operand {i}: "))
        if denom == 0:
            print("Division by zero.")
        result /= denom
    print(result)
else:
    print("Invalid operator!")