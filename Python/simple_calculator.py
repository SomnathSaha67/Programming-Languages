operator=input("Enter operator: + , - , * , / : ")
sum=0.0
difference=0.0
product=1.0
quotient=1
if operator=="+":
    n=int(input("Enter no. of operands: "))
    for i in range(1,n+1):
        operand=float(input("Enter value of operand",i,": "))
        sum+=operand
    print(sum)
else if operator=="-":
    n=int(input("Enter no. of operands: "))
    for i in range(1,n+1):
        operand=float(input("Enter value of operand",i,": "))
        difference-=operand
    print(difference)
else if operator=="*":
    n=int(input("Enter no. of operands: "))
    for i in range(1,n+1):
        operand=float(input("Enter value of operand",i,": "))
        product*=operand
    print(product)
else if operator=="/":
    n=int(input("Enter no. of operands: "))
    for i in range(1,n+1):
        operand=float(input("Enter value of operand",i,": "))
        quotient/=operand
    print(quotient)
else:
    print("Invalid Operator!") 
        