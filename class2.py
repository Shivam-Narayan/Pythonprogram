# without constructor __init__()
'''class faculty:
    def putdata(self):
        self.id = int(input ("Enter faculty id : "))
        self.name = input("Enter name : ")
        self.salary = float(input("Enter faculty salary : "))
    def display(self):
         print("Faculty id : ",self.id)
         print("Faculty name:",self.name)
         print("faculty salary:",self.salary)
a = faculty()
a.putdata()
a.display()'''

# with constructor __init__()
class faculty:
    def __init__(self):
        self.id = int(input ("Enter faculty id : "))
        self.name = input("Enter name : ")
        self.salary = float(input("Enter faculty salary : "))
    def display(self):
         print("Faculty id : ",self.id)
         print("Faculty name:",self.name)
         print("faculty salary:",self.salary)
a = faculty()
a.display()
