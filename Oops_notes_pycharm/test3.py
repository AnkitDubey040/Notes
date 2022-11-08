# we are able to easily acccess within class now we want that
# from person class in first file we want to use in this file

#hume pehli file ka use doosri mei karna hai

# SO WE IMPORT test1 file
import test1
print(test1) # isse test1 file ke sare result aa jayenge sare


#ques is to create object of person class of test1
objperson=test1.Person("shaka","laka",2000)
print(objperson.srname1)
# we directly created class here in this file and used it here
# also **** on ctrl+click on Person keyword pycharm will take me to test1 file and in Person class

# now let's class protected and private metyhods of test1:
print(objperson._name1)
print(objperson._Person__yob1)  # BOTH OF THese GIVES ME AN ERROR BECAUSE we have currently imported test3 in test1
# if we remove test3 import from test1 it works absolutely fine
#from fil 2  we have :

class Person1:
    _name = "andysurz"
    __srname = "demhsat"
    yob = 1983

    def _age(self,currentyr):
        return currentyr-self.yob

    def  __age1(self,currentyr):
        return currentyr - self.yob

obj1 = Person1()
print(obj1._age(2022))  #calling a protected function
print(obj1._Person1__age1(2022)) #calling a private function


class Employee(Person1):
    _name = "eadnbd"
    __srname="hjbfhcabbf"
    yob=3221

objemp1 = Employee()
print(objemp1)

print(objemp1.yob)

print(objemp1._name)

print(objemp1._Employee__srname) # now output from employee class only

#calling function of Paremt class thr object of EMp class
print(objemp1._age(2022))

print(objemp1._Person1__age1(2022)) # it successfully calls both these public,private and protected method




