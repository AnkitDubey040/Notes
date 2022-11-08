# INHERITANCE AND ACCESS :

class Person:
    # var outside any method :  (here we don't have to pass any parameter so)
    # GLOBAL VARIABLE
    _name = "andysurz"  #protected
    __srname = "demhsat"  # private
    yob = 1983            # public

obj1 = Person()
print(obj1)


class Employee(Person):
    pass
    # INHERITANC
    # we'll inherit Person class var
    # so ALL THE PROPERTIES of PERSON CLass are INHERITED
    # in the EMPLOYEE Class
    #EMPLOYEE = CHILD CLASS
    #PERSON + PARENT CLASS

objemp1 = Employee()
print(objemp1)

#now thr' emp class obj we acess person class var
print(objemp1.yob)    # IT IS PUBLIC SO EASILY INHERITED

#Inheriting PROTECTED MEMBER OF PERSON
print(objemp1._name)
#we can access this protected member

#INheriting private member
print(objemp1._Person__srname) # we access it this way

# if we would have written
# print(objemp1._Employee__srname)
# then it would not have worked


















