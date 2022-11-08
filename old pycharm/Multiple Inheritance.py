class Employee:
    leaves=6
    var =8
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


Ankit = Employee("Anknit Dubey",200000,"Sr.Analyst")

class Player:
    no_of_games=4
    var=9
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def printdetails(self):
        return f"Name is {self.name} , game is {self.game}  "
Ayush = Player("Ayush","Cricket")


class CoolProg(Employee,Player):   # multiple inheritance oeder is impoortant of inheriting
    lang="C++"

    def printlang(self):
        print(self.lang)

Sagar= CoolProg("Sagar",200000,"Executive")
prt=Sagar.details()
print(prt)
abc= Sagar.printlang()
print(abc)
print(Sagar.var)  #take var from Employee class as Employee class is inherited first
