def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def prod(a,b):
    return a*b
def div(a,b):
    if b!=0:
        return a/b
    else:
        return "Error:Division by zero"

def calculator():
    while True:
        print("1.addition")
        print("2.substraction")
        print("3.multiply")
        print("4.division")
        print("5.Exit")
        print("--------------------")
        choice=input("Enter a number from 1 to 4\n")
        if choice=='5':
            print("Invalid error")
            break

        num1=int(input("Enter 1st value"))
        num2=int(input("Enter 2nd value"))
        
        if choice=='1':
            print("Result:",add(num1,num2))
            break
        elif choice=='2':
          print("Result:",substract(num1,num2))
            break
        elif choice=='3':
            print("Result:",prod(num1,num2))
            break
        elif choice=='4':
            print("Result:",div(num1,num2))
            break
        else:
            print("Invalid error")
            break
print("Task1")
calculator()

