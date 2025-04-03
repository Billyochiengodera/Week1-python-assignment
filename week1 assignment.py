def calculator():
    
    print("Please enter the first number")
    num1 = float(input())
    print("please enter the second number")
    num2 =float(input())
    print("Please enter the operation you want to perform +,-,*,/")
    operation = input()
    if operation == "+":
        result = num1 + num2
        print(f"{num1}+{num2}={result}")
    elif operation == "-":
        result = num1 - num2
        print(f"{num1}-{num2}={result}")
    elif operation == "*":
        result = num1 * num2
        print(f"{num1}*{num2}={result}")
    elif operation == "/":
        if num2 != 0:
         result = num1 / num2
         print(f"{num1}/{num2}={result}")
        else:
         print("Error cannot devide by zero")
    else:
     print("Invalid operation")

calculator()



        
    







    