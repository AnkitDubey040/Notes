#

class ineuron:
    def students(self):
        print("print student details")

class class_type:
    def students(self):
         print("print class type of student")

def ineuron_external(a):
    a.students()

i=ineuron()
j=class_type()

ineuron_external(i)
ineuron_external(j)
'''
we are calling same func just changing the parameter and with 
change of parnameter the behaviour of func changes and it prints according to the 
object of the class that it belomgs to.
This func is a bridge to both classes


this is POLYMORPHISM
'''



#another   example of polymorphism
# one func can take two data types so behaviour change as data type
#This is called

'''POLYMORPHISM'''

'''
for int data type it is addition function
for str data type iot is concatenation function
'''

def test(a,b):
    return a+b
print(test(3,4))
print(test("andy "," loriies"))


