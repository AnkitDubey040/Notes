#PUBLIC , PRIVATE AND PROTECTED VARIABLES:


#*****this block after doing test3::::

# we are importing say employee class and Person1 class of test3 file here

# we want to import only 1 class of test3 in test1 file so we do :


#from test3 import Employee  #this will import employeee class only of test3
 # chalane se pehle ye upar wale ko band kar lena

# USING PERSON@ CLASS OF UTIL FILE :
# import util.util1    or we can use :
from util.util1 import Person2
objp2 = Person2("person2name","person2 srname",1232141)
print(objp2.srname1)


# ******content of test1 file::::
class Person:
    def __init__(self,name,srname,yob):
        self._name1=name #we marked it underscore to make it PROTECTED but here _ underscore before vaoable name means
        # it is protected
        self.srname1=srname
        self.__yob1=yob
        #by default they are all Public varibles or parameteres

andy = Person("Ankit","Dubey",2001)
# now if i want to access it :

print(andy.srname1) #srname1 is class variable
# i can access it anywhere as it is object of PUBLIC CLASS
# Now i want to restrict its access so : PUBLIC,PRIVATE,PROTECTED
# so we change access :  Access Specifiers

# we have applied _ in name1 var to make it protected
# so we can access it within a class not in any other packadge
print(andy._name1)

#__ double underscore means private


# print(andy.__yob1)

# this gives us an error as it is a Private object ,so we are unable to access it
# to call data which is private we need to tyoe :

print(andy._Person__yob1)
# now we are able to print PRIVATE Var so to acces private and protected we need to type in :
# (underscore)CLASSNAME(single or double underscore according to var)(Public or private var)
