#continued from last file ... now suppose in Employee class we
# want to add variables with same name as that of Person class and we want to
# see what happens while the Person class is being inherited


# also we create  method in parent class and use in child class
#ACCESS SPECIFIERS IN FUNCTIONS
class Person:
    # var outside any method :  (here we don't have to pass any parameter so)
    # GLOBAL VARIABLE
    _name = "andysurz"  #protected
    __srname = "demhsat"  # private
    yob = 1983            # public

    def _age(self,currentyr):
        return currentyr-self.yob

    def  __age1(self,currentyr):
        return currentyr - self.yob

obj1 = Person()
print(obj1._age(2022))  #calling a protected function
print(obj1._Person__age1(2022)) #calling a private function


class Employee(Person):
    _name = "eadnbd"
    __srname="hjbfhcabbf"
    yob=3221

objemp1 = Employee()
print(objemp1)
# we now get new value here
print(objemp1.yob)

print(objemp1._name)

#print(objemp1._Person__srname)
#it is from prev only as it has person in  it

print(objemp1._Employee__srname) # now output from employee class only

#calling function of Paremt class thr object of EMp class
print(objemp1._age(2022))

print(objemp1._Person__age1(2022)) # it successfully calls both these public,private and protected method

