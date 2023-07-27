

def divide(num1:float,num2:float):
    x = num1/num2
    return x

def multiply(num1:float,num2:float):
    x = num1 * num2
    return x

def addition(num1:float,num2:float):
    x = num1 + num2
    return x
def substract(num1:float,num2:float):
    x = num1 - num2
    return x

num1 = float(input("Enter num1: ")) 
num2 = float(input("Enter num2: "))

print(divide(num1,num2))
print(multiply(num1,num2))
print(addition(num1,num2))
print(substract(num1,num2))

