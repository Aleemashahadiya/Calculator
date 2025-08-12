print("Welcome to the calculator program")
a=int(input("enter the first number"))
b=int(input("enter the second number"))
while True:
    print("Choose an operation:")
    print("1=ADD")
    print("2=SUBTRACT")
    print("3=DIVISION")
    print("4=MULTIPLICATION")
    choice=int(input("enter your choice"))
    if choice==1:
        print("Result=",a+b)
    elif choice==2:
        print("Result=",a-b)
    elif choice==3:
        if b == 0:
            print("Division by zero is not allowed.")
        else:
            print("Result=",a/b)
    elif choice==4:
        print("Result=",a*b)
    elif choice==5:
        print("Exit")
        break
    else:
        print("Please enter the correct choice!")