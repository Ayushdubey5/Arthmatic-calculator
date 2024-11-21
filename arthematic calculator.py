 # python calculator

operator = input("enter an operator (+ - * /);="  )
num1 = float(input("enter the first number="))
num2 = float(input("enter the secod number="))

if operator == "+":
    Result = num1 + num2
    print (round(Result), 3)
elif operator == "-":
    Result = num1 - num2
    print (round(Result), 3)
elif operator == "*":
    Result = num1 * num2
    print (round(Result), 3)
elif operator == "/":
    Result = num1 / num2
    print (round(Result), 3)
else :
    print (f"{operator}is not valid" )