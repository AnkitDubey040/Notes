####self and _init_()

class Employee:
    leaves=6
    def __init__(self,name1,salary1,job1): #for creating sonstructors
        self.name=name1
        self.salary=salary1
        self.job=job1

    def details(self):    #method  I can use self for ankit or aysh rather than writing for both differently
        return f"Name is {self.name} , slaray is {self.salary} and job is {self.job} "

    @classmethod    #decorator      for changing leaves
    def changeleaves(cls,newleaves):
        cls.leaves=newleaves

    @classmethod
    def str(cls,string):        #alternatiove constructor
        list=string.split("-")#we use split func of slpit whose 1st item is karan 2nd item 40000 and 3 rd is peon
        return cls(list[0],list[1],list[2])




# ankit=Employee()  #instance
# ayush=Employee()  #instance
#
# ankit.name="Ankit The Smart"
# ankit.salary= 200000
# ankit.job="data analyst"
# ayush.name="Ayush the Dumb"
# ayush.salary= 20000
# ayush.job="Teacher"
#
#
# print(ankit.details())
# print(ayush.details())
# print(ankit.leaves)

####constructor  ---  init()

ankit=Employee("Ankit Dubey", 200000,"analyst") #these arguments go to init func
print(ankit.salary)

####changing class variables
Employee.leaves=4  #changing class variable which cannot be done by class instance
print(ankit.leaves)
# ankit.leaves=5
# print(Employee.leaves)# class variable not changed with instance
####now suppose i want to change leaves with methods so i do changes in class

ankit.changeleaves(12)
print(Employee.leaves) #now it's changes
print(ankit.leaves)

#####alternative constructor
#see class decorator 2nd wala

karan=Employee.str("karan-40000-peon") # we dont need 3args but only 1 arg
print(karan.salary)
print(karan.name)
print(karan.job)


