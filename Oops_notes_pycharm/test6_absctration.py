class Ineuron:
    __student = "data sc" #private var

    def student_m(self):
        print("The class of students: ", Ineuron.__student)

i=Ineuron()
i.student_m()

#i.__student() # will not work as we hide __student var in the Class Ineuron by making it Private
#it is called DATA ABSTRACTION --> we are not giving direct access to data
# to access we have to do:
print(i._Ineuron__student)

#we are using abstravction from long time everwhere...
#let's see logic behid list class ..hover over it goto option and jump to source
list()
print()