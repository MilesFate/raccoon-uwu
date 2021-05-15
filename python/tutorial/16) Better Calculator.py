#Gets first number
num1 = float(input("Enter first number: "))
#Gets the operator
op = input("Enter operator: ")
#Gets the second number
num2 = float(input("Enter another number: "))

#Does the Math
if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Invalid Operator")
