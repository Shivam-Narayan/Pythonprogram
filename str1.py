class country:
    def __init__(self,name,population):
        self.name = name
        self.population = population
    def __str__(self):
        return"population of {} is {}".format(self.name,self.population)

country_list = []
size = int(input('No of objects to be inserted: '))

for i in range(size):
    name = input("Enter the country name : ")
    population = int(input("Enter the population: "))
    obj = country(name,population)
    country_list.append(obj)

print("Country Details")
print('------------------------')
for i in country_list:
                     print(i)

print("***********************************")
print("country names with population greater than 50 crores")
print("-----------------------------------------------------------------------------")
for i in country_list:
                     if i.population>50:
                         print(i.name)
                     

                     
                     
                     
