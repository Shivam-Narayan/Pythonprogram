
"""n = int(input('Enter the number : '))
for i in range (1,n+1):
    print('*',end = " ")
     op ******
"""


"""n = int(input('Enter the number : '))
for i in range (1,n+1):
    print('*')
    
    # op *
         *
         *
         *
         *
"""

"""n = int(input("Enter the number :- "))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print() 
    
    # op *****
         *****
         *****
         *****
         *****
"""

'''nth = int(input("Enter the number of times:- "))
Start_value= int(input("Enter the Start value:- "))
for i in range(nth):
        for j in range(nth):
            print(Start_value,end=" ")
        Start_value+=1
        print()
        
        #op 1 1 1 1 1 
            2 2 2 2 2 
            3 3 3 3 3 
            4 4 4 4 4 
            5 5 5 5 5 
'''

'''n = int(input('Enter the number:- '))
for i in range(n):
    start_value = 1
    for j in range(n):
        print(start_value,end = " ")
        start_value += 1
    print()
    
    #op 1 2 3 4 5 
        1 2 3 4 5 
        1 2 3 4 5 
        1 2 3 4 5 
        1 2 3 4 5 
'''

'''n = int(input("Enter the number :- "))
for i in range(n,0,-1):
    for j in range(1,n+1):
        print(i,end = " ")
    print()

# op 7 7 7 7 7 7 7 
     6 6 6 6 6 6 6 
     5 5 5 5 5 5 5 
     4 4 4 4 4 4 4 
     3 3 3 3 3 3 3 
     2 2 2 2 2 2 2 
     1 1 1 1 1 1 1 '''

'''n = int(input("Enter the number :-"))
for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(j,end = " ")
    print()
    # op 5 4 3 2 1 
         5 4 3 2 1 
         5 4 3 2 1 
         5 4 3 2 1 
         5 4 3 2 1 '''
#ASCII VALUES.
#1. There are total of 128 characters.
#2. ASCII American standard code for information interchange
# A-Z -> 65-90
# a-z -> 97-122.
n = int(input("Enter the number :- "))
for i in range(1,n+1):
    for j in range(n,0,-1):
        print(chr(i+64),end = " ")
    print()
    # op