#INHERITANCE

'''

'''
# Parent Class
class Car:
    def __init__(self,body,engine,tyre): #constructor
        self.body =body
        self.engine =engine
        self.tyre=tyre
    def milage(self):
        print("milage of this car ")

c = Car("metal","hp211","mrf")

#Child Class
class Tata(Car): #inherited Car class to use it's features
    pass

#t = Tata()
#print(t)
'''
this gives me an error because it's askingfor args body, engine , tyre but we
do't have that in our tata class but in Car we have and since we inherited so it isa asking for it.
now we will give these values thr object of car class i.e. c object still t obj is giving error but not c object so 
c needs to be like t  so we have:
'''

t=Tata("solid","cv32","rain grip")
print(t)
#now no error so in inheritance obj of t should be like that of c
#it can also call methodof car class
t.milage()
