# OOPS   :
# CLASS ---> whenever we talk about animal say dog , cat , elephant etc... so when we say animal we don't
# know which animal  so class is an entity that we can
# design to get a blueprint...
# so it is blueprint of a real world entity

# --> in a prog lang or project we have diff component for diff things so multiple segments in project so to maintain
# boundary we need classes so that other person can understand code.
#segmentation

#OBJECT ---> instance(an example or case) of a class......so objects represent an entity that acually exist
# e.g. Animal is class and dog,cat,lion etc. would be it's object that actually exist

#constructor --> an inbuilt fun,method through which we pass, provide data to class

# to do that we create a method   def __init(self) which is a constructor    --> init is an initialization of a particular valuee to method
class Person:
    def __init__(self,name,srname,email,yob): # we have passed person details so class can be passed multiple times
        # self is a POINTER PArameter, always  first var pointer in constructor
        #all first parameter in func inside class=pointer
        self.name=name
        # both of these name are not same

        #self.yourvar = name
        #self.yourvar = name will not work here to make it work hume niche object call ke waqt bhi yhi pas karna hoga

        # matlab pehle wala name chalta hai object ke saath
        #  self is not a keyword
        self.srname=srname
        self.email=email
        self.yob=yob

# now we'll create  class variable  or object

ank_var= Person("ankit","dubey","ankit@1232141",2001)
sag_var= Person("saga","naka","s@1232141",7567)
zeb_var= Person("zebestian","weasely","weasly@1232141",7765)


#print(ank_var.yourvar)
print(ank_var.name)
print(ank_var.srname)
print(ank_var.email)
print(ank_var.yob)
print(sag_var.name)
print(sag_var.srname)
print(zeb_var.email)
print(zeb_var.yob)


# to check type of var :
print(type(sag_var))  #=> object



# __init__ function ki tarah aur bhi functions hotye hai python nmei
# __init__,__str__,__retr__,_getter__ etc.

