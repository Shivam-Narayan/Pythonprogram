def  add(x,y):
    print("Sum of {} & {} is {}".format(x,y,x+y))

def sub(x,y):
    print("Difference of {} & {} is {}".format(x,y,x-y))

def mul(x,y):
    print("Product of  {} & {} is {}".format(x,y,x*y))

def div(x,y):
    print("Division of {} & {} is {}".format(x,y,x/y))

#Menu driven Program
    print("Welcome to calculater Project")
    print("------------------------------------------")

print("add,sub,mul,div")
choice = int(input("Enter choice : "))
x = int(input("Enter first number : " ))
y = int(input("Enter second number : "))
if choice == 1:
   add(x,y)

elif choice == 2:
    sub(x,y)

elif choice == 3:
     mul(x,y)

elif choice == 4:
    div(x,y)

elif choice == 5:
    print("Thank You")
    exit()

else:
    print("INVALID CHOICE")
