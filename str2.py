class employee:
    def __init__(self,eid,name,salary):
        self.eid = eid
        self.name = name
        self.salary = salary

     def __str__(self):
         return "employee {} having id {} is earning {} lpa".format.(self.name,self.eid,self.salary)

e_list = []
size = int(input("enter the size :"))

for i in range(size):
    eid = int(input("enter the id : "))
    name = input("enter name : ")
    salary = float(input("enter salary : "))
    obj = employee(id,name,salary)
    emp_list.append(obj)

print("Employee Details")
for i in emp_list:
    print(i)

print("************************************")

print('Employee name whose salary is greater than 3.5 LPA")
      for  e in emp_list:
            if e.salary>3.5:
      print(e.name)

print("*************************************************")

      print("Employee names starting with letter A")
      for e in emp_list:
      if e.name[0] ='a':
      print(e.name)
    
