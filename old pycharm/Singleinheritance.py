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

    @staticmethod
    def static_method(string):  #we pack it inside class if we want only class instance to use it
        print("This is very well done" + string)
        return 0

class Programmer(Employee):
    def __init__(self, name1, salary1, job1,languages):  # for creating sonstructors
        self.name = name1
        self.salary = salary1
        self.job = job1  #constructor --now we'll use super() here
        self.languages= languages

    def printprog(self):
        return f"The programmer name is {self.name},slary is {self.salary} and job is {self.job} and lang is {self.languages}"
                                             # Programmer child class inherits Employee class


karan=Employee.str("karan-40000-peon") # we dont need 3args but only 1 arg
print(karan.static_method(" AnkitDubey"))
Ayush =Programmer("Ayush", 333, "Programmer sr",["Python"]) #var of inherited class
print(Ayush.printprog())    #working of inheritance